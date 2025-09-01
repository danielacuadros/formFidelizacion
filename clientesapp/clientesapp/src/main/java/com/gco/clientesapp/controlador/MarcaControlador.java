package com.gco.clientesapp.controlador;

import com.gco.clientesapp.modelo.Marca;
import com.gco.clientesapp.servicio.MarcaServicio;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/marcas")
@CrossOrigin(origins = "*")   // ← añade esto
public class MarcaControlador {
    private final MarcaServicio marcaServicio;
    public MarcaControlador(MarcaServicio marcaServicio) { this.marcaServicio = marcaServicio; }

    @GetMapping
    public List<Marca> obtenerTodasLasMarcas() {
        return marcaServicio.obtenerTodasLasMarcas();
    }

    @GetMapping("/{id}")
    public Marca obtenerMarcaPorId(@PathVariable Long id) {
        return marcaServicio.obtenerMarcaPorId(id);
    }
}
