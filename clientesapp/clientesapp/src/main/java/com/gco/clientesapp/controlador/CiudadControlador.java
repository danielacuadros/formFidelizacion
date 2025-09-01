package com.gco.clientesapp.controlador;

import com.gco.clientesapp.modelo.Ciudad;
import com.gco.clientesapp.servicio.CiudadServicio;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/ciudades")
public class CiudadControlador {

    private final CiudadServicio ciudadServicio;

    public CiudadControlador(CiudadServicio ciudadServicio) {
        this.ciudadServicio = ciudadServicio;
    }

    @GetMapping
    public List<Ciudad> obtenerTodasLasCiudades() {
        return ciudadServicio.obtenerTodasLasCiudades();
    }

    @GetMapping("/paises")
    public List<String> obtenerPaises() {
        return ciudadServicio.obtenerPaises();
    }

    @GetMapping("/departamentos/{pais}")
    public List<String> obtenerDepartamentosPorPais(@PathVariable String pais) {
        return ciudadServicio.obtenerDepartamentosPorPais(pais);
    }

    @GetMapping("/por-departamento/{departamento}")
    public List<Ciudad> obtenerCiudadesPorDepartamento(@PathVariable String departamento) {
        return ciudadServicio.obtenerCiudadesPorDepartamento(departamento);
    }
}
