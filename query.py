"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

>>> brand = Brand.query.get(8)
>>> print brand
<id=8, name=u'Austin', founded=1905, HQ=u'Longbridge, England', disc=1987


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

>>> models = Model.query.filter(Model.name == 'Corvette', 
                                Model.brand_name == 'Chevrolet').all()
>>> for model in models:
...     print model
...
<id=5, year=1953, brand_name=u'Chevrolet', name=u'Corvette'>
<id=6, year=1954, brand_name=u'Chevrolet', name=u'Corvette'>
<id=8, year=1955, brand_name=u'Chevrolet', name=u'Corvette'>
<id=10, year=1956, brand_name=u'Chevrolet', name=u'Corvette'>
<id=11, year=1957, brand_name=u'Chevrolet', name=u'Corvette'>
<id=13, year=1958, brand_name=u'Chevrolet', name=u'Corvette'>
<id=17, year=1959, brand_name=u'Chevrolet', name=u'Corvette'>
<id=20, year=1960, brand_name=u'Chevrolet', name=u'Corvette'>
<id=26, year=1961, brand_name=u'Chevrolet', name=u'Corvette'>
<id=28, year=1962, brand_name=u'Chevrolet', name=u'Corvette'>
<id=38, year=1963, brand_name=u'Chevrolet', name=u'Corvette'>
<id=39, year=1964, brand_name=u'Chevrolet', name=u'Corvette'>

# Get all models that are older than 1960.

>>> old_models = Model.query.filter(Model.year < 1960).all()
>>> for model in old_models:
...     print model
...
<id=1, year=1909, brand_name=u'Ford', name=u'Model T'>
<id=2, year=1926, brand_name=u'Chrysler', name=u'Imperial'>
<id=3, year=1948, brand_name=u'Citro\xebn', name=u'2CV'>
<id=4, year=1950, brand_name=u'Hillman', name=u'Minx Magnificent'>
<id=5, year=1953, brand_name=u'Chevrolet', name=u'Corvette'>
<id=6, year=1954, brand_name=u'Chevrolet', name=u'Corvette'>
<id=7, year=1954, brand_name=u'Cadillac', name=u'Fleetwood'>
<id=8, year=1955, brand_name=u'Chevrolet', name=u'Corvette'>
<id=9, year=1955, brand_name=u'Ford', name=u'Thunderbird'>
<id=10, year=1956, brand_name=u'Chevrolet', name=u'Corvette'>
<id=11, year=1957, brand_name=u'Chevrolet', name=u'Corvette'>
<id=12, year=1957, brand_name=u'BMW', name=u'600'>
<id=13, year=1958, brand_name=u'Chevrolet', name=u'Corvette'>
<id=14, year=1958, brand_name=u'BMW', name=u'600'>
<id=15, year=1958, brand_name=u'Ford', name=u'Thunderbird'>
<id=16, year=1959, brand_name=u'Austin', name=u'Mini'>
<id=17, year=1959, brand_name=u'Chevrolet', name=u'Corvette'>
<id=18, year=1959, brand_name=u'BMW', name=u'600'>



# Get all brands that were founded after 1920.

# Get all models with names that begin with "Cor".

# Get all brands with that were founded in 1903 and that are not yet discontinued.

# Get all brands with that are either discontinued or founded before 1950.

# Get any model whose brand_name is not Chevrolet.

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    pass

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
