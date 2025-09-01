package com.gco.clientesapp.controlador;

import com.gco.clientesapp.modelo.Cliente;
import com.gco.clientesapp.servicio.ClienteServicio;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/clientes")
@CrossOrigin(origins = "*")
public class ClienteControlador {

    private final ClienteServicio clienteServicio;

    public ClienteControlador(ClienteServicio clienteServicio) {
        this.clienteServicio = clienteServicio;
    }

    @GetMapping
    public List<Cliente> listarClientes() {
        return clienteServicio.listarClientes();
    }

    @PostMapping
    public ResponseEntity<?> guardarCliente(@RequestBody Map<String, Object> clienteData) {
        return clienteServicio.guardarCliente(clienteData);
    }
}
