from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

import crud
import schemas
from data_base.engine import SessionLocal

app = FastAPI()


def get_db_session() -> Session:
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


@app.get("/")
def root() -> dict:
    routes = ["/docs", "/redoc", "/products/", "/products/{product_id}"]
    return {"message": "Available endpoints", "routes": routes}


@app.get("/products/", response_model=list[schemas.ProductRetrieveScheme])
def retrieve_all_products(db_session: Session = Depends(get_db_session)):
    return crud.get_all_products(db_session)


@app.post("/products/", response_model=schemas.ProductRetrieveScheme)
def create_product(
    product_data: schemas.ProductCreateScheme,
    db_session: Session = Depends(get_db_session),
):
    try:
        return crud.create_product(db_session=db_session, product=product_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/products/{product_id}", response_model=schemas.ProductRetrieveScheme)
def retrieve_single_product(
    product_id: int, db_session: Session = Depends(get_db_session)
):
    db_product = crud.get_single_product(db_session=db_session, product_id=product_id)
    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} not found"
        )
    return db_product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_product(
    product_id: int, db_session: Session = Depends(get_db_session)
):
    db_product = crud.get_single_product(db_session=db_session, product_id=product_id)
    if not db_product:
        raise HTTPException(
            status_code=404, detail=f"Product with id {product_id} not found"
        )

    db_session.delete(db_product)
    db_session.commit()

    return None


@app.put("/products/{product_id}", response_model=schemas.ProductRetrieveScheme)
def update_product(
    product_id: int,
    product_update: schemas.ProductBaseScheme,
    db_session: Session = Depends(get_db_session),
):
    updated_product = crud.update_single_product(
        db_session=db_session, product_id=product_id, product_scheme=product_update
    )

    # Check if the product was not found (based on JSONResponse from crud)
    if isinstance(updated_product, dict) and "error" in updated_product:
        raise HTTPException(status_code=404, detail=updated_product["error"])

    return updated_product
