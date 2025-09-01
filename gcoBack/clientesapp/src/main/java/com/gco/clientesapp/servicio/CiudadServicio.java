package com.gco.clientesapp.servicio;

import com.gco.clientesapp.modelo.Ciudad;
import com.gco.clientesapp.repositorio.CiudadRepositorio;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CiudadServicio {

    private final CiudadRepositorio ciudadRepositorio;

    public CiudadServicio(CiudadRepositorio ciudadRepositorio) {
        this.ciudadRepositorio = ciudadRepositorio;
    }

    public List<Ciudad> obtenerTodasLasCiudades() {
        return ciudadRepositorio.findAll();
    }

    public List<String> obtenerPaises() {
        return ciudadRepositorio.findDistinctPaises();
    }

    public List<String> obtenerDepartamentosPorPais(String pais) {
        return ciudadRepositorio.findDepartamentosByPais(pais);
    }

    public List<Ciudad> obtenerCiudadesPorDepartamento(String departamento) {
        return ciudadRepositorio.findByDepartamentoOrderByNombreCiudad(departamento);
    }
}
