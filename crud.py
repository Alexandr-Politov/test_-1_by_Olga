from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT
from fastapi.responses import JSONResponse
from data_base import models
import schemas


def get_all_products(db_session: Session):
    return db_session.query(models.DBProduct).all()


def get_single_product(db_session: Session, product_id: int):
    return (
        db_session.query(models.DBProduct)
        .filter(models.DBProduct.id == product_id)
        .first()
    )


def delete_product(db_session: Session, product_id: int):
    db_product = (
        db_session.query(models.DBProduct)
        .filter(models.DBProduct.id == product_id)
        .first()
    )
    if db_product:
        db_session.delete(db_product)
        db_session.commit()
        return JSONResponse(status_code=HTTP_204_NO_CONTENT)
    return JSONResponse(content={"error": "Product not found"}, status_code=404)


def create_product(db_session: Session, product_scheme: schemas.ProductCreateScheme):
    db_product = models.DBProduct(
        name=product_scheme.name,
        description=product_scheme.description,
        price=product_scheme.price,
    )
    db_session.add(db_product)
    db_session.commit()
    db_session.refresh(db_product)
    return db_product


def update_single_product(
    db_session: Session, product_id: int, product_scheme: schemas.ProductBaseScheme
):
    db_product = (
        db_session.query(models.DBProduct)
        .filter(models.DBProduct.id == product_id)
        .first()
    )
    if not db_product:
        return JSONResponse(content={"error": "Product not found"}, status_code=404)

    # Update fields
    db_product.name = product_scheme.name
    db_product.description = product_scheme.description
    db_product.price = product_scheme.price

    db_session.commit()
    db_session.refresh(db_product)
    return db_product
