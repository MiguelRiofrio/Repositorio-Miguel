using Models.Entidades;
using System;
using System.Collections.Generic;
using System.Text;

namespace Data.Interfaz.IRepositorio
{
    public interface IEspecialidadRepositorio :IRepositorioGenerico<Especialidad>
    {
        void Actualizar(Especialidad especialidad);
    }
}
