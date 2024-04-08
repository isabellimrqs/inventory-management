from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import (supplier_pydantic, supplier_pydanticIn, Supplier, product_pydanticIn, product_pydantic, Product)

app = FastAPI()

@app.get('/')
def index():
    return {"Msg": "Go to /docs for the API documentation"}

@app.post('/supplier')
async def add_supplier(supplier_info: supplier_pydanticIn):
    supplier_obj = await Supplier.create(**supplier_info.dict(exclude_unset=True))
    response = await supplier_pydantic.from_tortoise_orm(supplier_obj)
    return {"status": "ok", "data" : response}

@app.get('/supplier')
async def get_all_suppliers():
    response = await supplier_pydantic.from_queryset(Supplier.all())
    return {"status": "ok", "data" : response}

@app.get('/supplier/{supplier_id}')
async def get_specific_supplier(supplier_id: int):
    response = await supplier_pydantic.from_queryset_single(Supplier.get(id = supplier_id))
    return {"status": "ok", "data":response}

@app.put('/supplier/{supplier_id}')
async def update_supplier(supplier_id: int, update_info: supplier_pydanticIn):
    supplier = await Supplier.get(id = supplier_id)
    update_info = update_info.dict(exclude_unset=True)
    supplier.name = update_info['name']
    supplier.company = update_info['company']
    supplier.phone = update_info['phone']
    supplier.email = update_info['email']
    await supplier.save()
    response = await supplier_pydantic.from_tortoise_orm(supplier)
    return {"status": "ok", "data" : response}

@app.delete('/supplier/{supplier_id}')
async def delete_supplier(supplier_id: int):
    await Supplier.filter(id=supplier_id).delete()
    return {"status": "ok"}

@app.post('/product/{supplier_id}')
async def add_product(supplier_id: int, products_details: product_pydanticIn):
    supplier = await Supplier.get(id = supplier_id)
    products_details = products_details.dict(exclude_unset = True)
    products_details['revenue'] += products_details['quantity_sold'] * products_details['unit_price']
    product_obj = await Product.create(**products_details, supplied_by = supplier)
    response = await product_pydantic.from_tortoise_orm(product_obj)
    return {"status": "ok", "data" : response}

@app.get('/product')
async def all_products():
    response = await product_pydantic.from_queryset(Product.all())
    return {"status": "ok", "data" : response}

@app.get('/product/{id}')
async def specific_product(id: int):
    response = await product_pydantic.from_queryset_single(Product.get(id = id))
    return {"status": "ok", "data" : response}



@app.put('/product/{id}')
async def update_product(id: int, update_info: product_pydanticIn):
    product = await Product.get(id = id)
    update_info = update_info.dict(exclude_unset =True)
    product.name = update_info['name']
    product.quantity_in_stock = update_info['quantity_in_stock']
    product.quantity_sold = update_info['quantity_sold']
    product.unit_price = update_info['unit_price']
    product.revenue = update_info['quantity_sold'] * update_info['unit_price']
    await product.save()
    response = await product_pydantic.from_tortoise_orm(product)
    return {"status": "ok", "data" : response}

@app.delete('/product/{id}')
async def delete_product(id: int):
    await Product.filter(id=id).delete()
    return {"status": "ok"}




register_tortoise(
    app, 
    db_url = "sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas = True,
    add_exception_handlers = True
)