#module: app.db.models.MovimientoORM
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.domain.models.movimiento import TipoMovimiento

from app.db.models.base import EntityBase

# class TipoMovimiento(PyEnum):
#     ingreso = "ingreso"
#     egreso = "egreso"
#     traslado = "traslado"

class MovimientoORM(EntityBase):
    __tablename__ = "movimientos"
    __table_args__ = {'extend_existing': True}
    
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    deposito_origen_id = Column(Integer, ForeignKey("depositos.id"), nullable=True)
    deposito_destino_id = Column(Integer, ForeignKey("depositos.id"), nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)
    tipo = Column(Enum(TipoMovimiento), nullable=False)

    producto = relationship("ProductoORM", back_populates="movimientos")
    deposito_origen = relationship("DepositoORM", foreign_keys=[deposito_origen_id], back_populates="movimientos_origen")
    deposito_destino = relationship("DepositoORM", foreign_keys=[deposito_destino_id], back_populates="movimientos_destino")
    usuario = relationship("UsuarioORM")