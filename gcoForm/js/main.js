import { cargarUbicaciones } from "./ubicacion.js";
import { soloNumeros, esMayorDeEdad } from "./validacion.js";

document.addEventListener("DOMContentLoaded", () => {
  cargarUbicaciones();

  const docInput = document.getElementById("numero_identificacion");
  soloNumeros(docInput);

  const form = document.getElementById("clienteForm");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const fecha = document.getElementById("fecha_nacimiento").value;
    if (!esMayorDeEdad(fecha)) {
      Swal.fire({
        icon: "warning",
        title: "Validación",
        text: "El cliente debe ser mayor de 18 años."
      });
      return;
    }

    const cliente = {
      tipo_identificacion: document.getElementById("tipo_identificacion").value,
      numero_identificacion: document.getElementById("numero_identificacion").value.trim(),
      nombres: document.getElementById("nombres").value.trim(),
      apellidos: document.getElementById("apellidos").value.trim(),
      fecha_nacimiento: fecha,
      direccion: document.getElementById("direccion").value.trim(),
      id_ciudad: parseInt(document.getElementById("ciudad").value),
      id_marca: parseInt(document.getElementById("marca").value)
    };

    const camposRequeridos = [
      { campo: 'tipo_identificacion', nombre: 'Tipo de identificación' },
      { campo: 'numero_identificacion', nombre: 'Número de identificación' },
      { campo: 'nombres', nombre: 'Nombres' },
      { campo: 'apellidos', nombre: 'Apellidos' },
      { campo: 'fecha_nacimiento', nombre: 'Fecha de nacimiento' },
      { campo: 'direccion', nombre: 'Dirección' },
      { campo: 'id_ciudad', nombre: 'Ciudad' },
      { campo: 'id_marca', nombre: 'Marca' }
    ];

    for (const item of camposRequeridos) {
      const valor = cliente[item.campo];

      if (item.campo === 'id_ciudad' || item.campo === 'id_marca') {
        if (!valor || isNaN(valor) || valor <= 0) {
          Swal.fire({
            icon: "warning",
            title: "Campo requerido",
            text: `Por favor completa: ${item.nombre}`
          });
          return;
        }
      } else {
        if (!valor || (typeof valor === 'string' && valor.trim() === '')) {
          Swal.fire({
            icon: "warning",
            title: "Campo requerido",
            text: `Por favor completa: ${item.nombre}`
          });
          return;
        }
      }
    }

    try {
      const resp = await fetch("http://localhost:8080/api/cliente", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(cliente),
      });

      if (!resp.ok) {
        const errorText = await resp.text();
        console.error("Error del servidor:", errorText);

        let errorMsg = "Error desconocido";

        try {
          const errorJson = JSON.parse(errorText);

          if (
            errorJson.detalle &&
            errorJson.detalle.includes("Duplicate entry") &&
            errorJson.detalle.includes("numero_identificacion")
          ) {
            errorMsg = "El número de identificación ya está registrado. Intenta con uno diferente.";
          } else {
            errorMsg = errorJson.error || errorJson.message || errorText;
          }
        } catch {
          errorMsg = errorText;
        }

        throw new Error(`Error ${resp.status}: ${errorMsg}`);
      }

      const clienteGuardado = await resp.json();

      const ciudadNombre = document.getElementById("ciudad").selectedOptions[0]?.text || "N/A";
      const marcaNombre = document.getElementById("marca").selectedOptions[0]?.text || "N/A";

      Swal.fire({
        icon: "success",
        title: "¡Cliente registrado exitosamente!",
        html: `<strong>${cliente.nombres} ${cliente.apellidos}</strong><br>
               Ciudad: ${ciudadNombre}<br>
               Marca: ${marcaNombre}<br>
               ID: ${clienteGuardado.id}`,
        showConfirmButton: true,
        confirmButtonText: "Continuar"
      });

      form.reset();
      resetearCombos();

    } catch (err) {
      console.error("Error completo:", err);
      Swal.fire({
        icon: "error",
        title: "Error al registrar",
        text: err.message || "Hubo un problema al guardar los datos. Revisa la consola para más detalles."
      });
    }
  });
});

function resetearCombos() {
  const paisSelect = document.getElementById("pais");
  const deptoSelect = document.getElementById("departamento");
  const ciudadSelect = document.getElementById("ciudad");

  deptoSelect.innerHTML = "<option value=''>Seleccione departamento...</option>";
  ciudadSelect.innerHTML = "<option value=''>Seleccione ciudad...</option>";
  deptoSelect.disabled = true;
  ciudadSelect.disabled = true;

  if (paisSelect.value) {
    paisSelect.selectedIndex = 0;
  }
}
