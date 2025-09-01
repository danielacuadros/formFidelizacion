package com.gco.clientesapp.servicio;

import com.gco.clientesapp.modelo.Cliente;
import com.gco.clientesapp.repositorio.ClienteRepositorio;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class ClienteServicio {

    private final ClienteRepositorio clienteRepositorio;

    public ClienteServicio(ClienteRepositorio clienteRepositorio) {
        this.clienteRepositorio = clienteRepositorio;
    }

    public List<Cliente> listarClientes() {
        return clienteRepositorio.findAll();
    }

    public ResponseEntity<?> guardarCliente(Map<String, Object> clienteData) {
        try {
            String[] camposRequeridos = {"tipo_identificacion", "numero_identificacion", "nombres", "apellidos", "fecha_nacimiento", "direccion"};
            for (String campo : camposRequeridos) {
                Object valor = clienteData.get(campo);
                if (valor == null || valor.toString().trim().isEmpty()) {
                    return ResponseEntity.badRequest()
                            .body(Map.of("error", "Campo requerido faltante: " + campo));
                }
            }

            Cliente cliente = new Cliente();
            cliente.setTipoIdentificacion((String) clienteData.get("tipo_identificacion"));
            cliente.setNumeroIdentificacion((String) clienteData.get("numero_identificacion"));
            cliente.setNombres((String) clienteData.get("nombres"));
            cliente.setApellidos((String) clienteData.get("apellidos"));
            cliente.setFechaNacimiento(LocalDate.parse((String) clienteData.get("fecha_nacimiento")));
            cliente.setDireccion((String) clienteData.get("direccion"));

            if (clienteData.get("id_ciudad") != null) {
                try {
                    Long idCiudad = Long.valueOf(clienteData.get("id_ciudad").toString());
                    if (idCiudad <= 0) {
                        return ResponseEntity.badRequest()
                                .body(Map.of("error", "ID de ciudad debe ser mayor a 0"));
                    }
                    cliente.setIdCiudad(idCiudad);
                } catch (NumberFormatException e) {
                    return ResponseEntity.badRequest()
                            .body(Map.of("error", "ID de ciudad inválido: " + clienteData.get("id_ciudad")));
                }
            } else {
                return ResponseEntity.badRequest()
                        .body(Map.of("error", "Ciudad es requerida"));
            }

            if (clienteData.get("id_marca") != null) {
                try {
                    Long idMarca = Long.valueOf(clienteData.get("id_marca").toString());
                    if (idMarca <= 0) {
                        return ResponseEntity.badRequest()
                                .body(Map.of("error", "ID de marca debe ser mayor a 0"));
                    }
                    cliente.setIdMarca(idMarca);
                } catch (NumberFormatException e) {
                    return ResponseEntity.badRequest()
                            .body(Map.of("error", "ID de marca inválido: " + clienteData.get("id_marca")));
                }
            } else {
                return ResponseEntity.badRequest()
                        .body(Map.of("error", "Marca es requerida"));
            }

            Cliente clienteGuardado = clienteRepositorio.save(cliente);

            Map<String, Object> respuesta = new HashMap<>();
            respuesta.put("cliente", clienteGuardado);
            respuesta.put("mensaje", "Cliente registrado exitosamente");
            respuesta.put("id", clienteGuardado.getId());

            return ResponseEntity.ok(respuesta);

        } catch (Exception e) {
            return ResponseEntity.internalServerError()
                    .body(Map.of(
                            "error", "Error interno del servidor",
                            "detalle", e.getMessage(),
                            "tipo", e.getClass().getSimpleName()
                    ));
        }
    }
}
