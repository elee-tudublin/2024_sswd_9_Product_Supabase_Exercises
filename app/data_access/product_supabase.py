# import the model class
from app.models.product import Product
from starlette.config import Config
from supabase import create_client, Client


# Load environment variables from .env
config = Config(".env")

db_url: str = config("SUPABASE_URL")
db_key: str = config("SUPABASE_KEY")

supabase: Client = create_client(db_url, db_key)


# get all products
def dataGetProducts():
    response = (supabase.table("product")
                .select("*")
                .order("title", desc=False)
                .execute()
    )

    return response.data

# get product by id
def dataGetProduct(id):
    # select * from product where id = id 
    response = (
        supabase.table("product")
        .select("*")
        .eq("id", id)
        .execute()
    )
    return response.data[0]

# update product
def dataUpdateProduct(product: Product) :
    # pass params individually
    #response = supabase.table("product").upsert({"id": product.id, "category_id": product.category_id, "title": product.title, "thumbnail": product.thumbnail, "stock": product.stock, "price": product.price}).execute()
    response = (
        supabase.table("product")
        .upsert(product.dict()) # convert product object to dict - required by Supabase
        .execute()
    )
    # result is 1st item in the list
    return response.data[0]

# add product, accepts product object
def dataAddProduct(product: Product) :
    response = (
        supabase.table("product")
        .insert(product.dict()) # convert product object to dict - required by Supabase
        .execute()
    )
    # result is 1st item in the list
    return response.data[0]

# get all categories
def dataGetCategories():
    response = (supabase.table("category")
                .select("*")
                .order("name", desc=False)
                .execute()
    )

    return response.data


# delete product by id
def dataDeleteProduct(id):
    # select * from product where id = id 
    response = (
        supabase.table("product")
        .delete()
        .eq('id', id)
        .execute()
    )
    return response.data