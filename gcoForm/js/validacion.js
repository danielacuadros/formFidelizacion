// validacion.js

export function soloNumeros(input) {
  input.addEventListener("input", () => {
    input.value = input.value.replace(/\D/g, "");
  });
}

export function esMayorDeEdad(fechaStr) {
  if (!fechaStr) return false;

  const fechaNac = new Date(fechaStr);
  const hoy = new Date();

  let edad = hoy.getFullYear() - fechaNac.getFullYear();
  const m = hoy.getMonth() - fechaNac.getMonth();

  if (m < 0 || (m === 0 && hoy.getDate() < fechaNac.getDate())) {
    edad--;
  }

  return edad >= 18;
}
