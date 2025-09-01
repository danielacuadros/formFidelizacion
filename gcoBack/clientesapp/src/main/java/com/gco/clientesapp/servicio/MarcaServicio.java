package com.gco.clientesapp.servicio;

import com.gco.clientesapp.modelo.Marca;
import com.gco.clientesapp.repositorio.MarcaRepositorio;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MarcaServicio {

    private final MarcaRepositorio marcaRepositorio;

    public MarcaServicio(MarcaRepositorio marcaRepositorio) {
        this.marcaRepositorio = marcaRepositorio;
    }

    public List<Marca> obtenerTodasLasMarcas() {
        return marcaRepositorio.findAllByOrderByNombreMarca();
    }

    public Marca obtenerMarcaPorId(Long id) {
        return marcaRepositorio.findById(id).orElse(null);
    }
}
