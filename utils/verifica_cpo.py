def is_cpo(usuario):
    return usuario.groups.filter(name="CPO").exists()