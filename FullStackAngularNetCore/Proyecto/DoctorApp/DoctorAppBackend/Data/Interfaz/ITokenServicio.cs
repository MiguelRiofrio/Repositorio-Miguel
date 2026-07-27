using Models.Entidades;
using System;
using System.Collections.Generic;
using System.Text;

namespace Data.Interfaz
{
    public interface ITokenServicio
    {
        string CrearToken(Usuario usuario);
    }
}
