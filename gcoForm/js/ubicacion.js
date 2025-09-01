export async function cargarUbicaciones() {
  const paisSelect = document.getElementById("pais");
  const deptoSelect = document.getElementById("departamento");
  const ciudadSelect = document.getElementById("ciudad");
  const marcaSelect = document.getElementById("marca");

  if (!paisSelect || !deptoSelect || !ciudadSelect || !marcaSelect) {
    console.warn("Faltan selects requeridos en el DOM");
    return;
  }

  try {
  
    const respPaises = await fetch("http://localhost:8080/api/ciudades/paises");
    const paises = await respPaises.json();


    paisSelect.innerHTML = "<option value=''>Seleccione país...</option>";
    paises.forEach((pais) => {
      const opt = document.createElement("option");
      opt.value = pais;
      opt.textContent = pais;
      paisSelect.appendChild(opt);
    });

  
    const respMarcas = await fetch("http://localhost:8080/api/marcas");
    const marcas = await respMarcas.json();

    marcaSelect.innerHTML = "<option value=''>Seleccione marca...</option>";
    marcas.forEach((marca) => {
      const opt = document.createElement("option");
      opt.value = marca.idMarca;
      opt.textContent = marca.nombreMarca;
      marcaSelect.appendChild(opt);
    });
  } catch (error) {
    console.error("Error cargando datos del backend:", error);
    cargarDatosEstaticos();
  }

  paisSelect.addEventListener("change", async () => {
    const pais = paisSelect.value;
    deptoSelect.innerHTML = "<option value=''>Seleccione departamento...</option>";
    ciudadSelect.innerHTML = "<option value=''>Seleccione ciudad...</option>";

    if (!pais) {
      deptoSelect.disabled = true;
      ciudadSelect.disabled = true;
      return;
    }

    try {
      const resp = await fetch(`http://localhost:8080/api/ciudades/departamentos/${encodeURIComponent(pais)}`);
      const departamentos = await resp.json();

      departamentos.forEach((depto) => {
        const opt = document.createElement("option");
        opt.value = depto;
        opt.textContent = depto;
        deptoSelect.appendChild(opt);
      });

      deptoSelect.disabled = false;
      ciudadSelect.disabled = true;
    } catch (error) {
      console.error("Error cargando departamentos:", error);
    }
  });

  deptoSelect.addEventListener("change", async () => {
    const departamento = deptoSelect.value;
    ciudadSelect.innerHTML = "<option value=''>Seleccione ciudad...</option>";

    if (!departamento) {
      ciudadSelect.disabled = true;
      return;
    }

    try {
      const resp = await fetch(`http://localhost:8080/api/ciudades/por-departamento/${encodeURIComponent(departamento)}`);
      const ciudades = await resp.json();

      ciudades.forEach((ciudad) => {
        const opt = document.createElement("option");
        opt.value = ciudad.idCiudad;
        opt.textContent = ciudad.nombreCiudad;
        ciudadSelect.appendChild(opt);
      });

      ciudadSelect.disabled = false;
    } catch (error) {
      console.error("Error cargando ciudades:", error);
    }
  });

  deptoSelect.disabled = true;
  ciudadSelect.disabled = true;
}


function cargarDatosEstaticos() {
  const marcaSelect = document.getElementById("marca");
  const marcas = [
    { id: 1, nombre: "NAF NAF" },
    { id: 2, nombre: "RIFLE" },
    { id: 3, nombre: "AMERICANINO" },
    { id: 4, nombre: "CHEVIGNON" },
    { id: 5, nombre: "ESPRIT" },
    { id: 6, nombre: "AMERICAN EAGLE" },
    { id: 7, nombre: "MANGO" }
  ];

  marcaSelect.innerHTML = "<option value=''>Seleccione marca...</option>";
  marcas.forEach((marca) => {
    const opt = document.createElement("option");
    opt.value = marca.id;
    opt.textContent = marca.nombre;
    marcaSelect.appendChild(opt);
  });
}
