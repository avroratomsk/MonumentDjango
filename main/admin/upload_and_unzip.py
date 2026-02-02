from PIL import Image
from pytils.translit import slugify
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
import openpyxl
import os
import zipfile
from shop.models import  ColorProduct, Product, Category, ProductImage, ShopSettings
from main.settings import BASE_DIR



