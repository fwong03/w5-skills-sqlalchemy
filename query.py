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
<id=8, name=u'Austin', founded=1905, HQ=u'Longbridge, England', disc=1987>


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

>>> youngbrands = Brand.query.filter(Brand.founded > 1920).all()
>>> for brand in youngbrands:
...     print brand
...
<id=2, name=u'Chrysler', founded=1925, HQ=u'Auburn Hills, Michigan', disc=None>
<id=9, name=u'Fairthorpe', founded=1954, HQ=u'Chalfont St Peter, Buckinghamshire', disc=1976>
<id=11, name=u'Pontiac', founded=1926, HQ=u'Detroit, MI', disc=2010>
<id=14, name=u'Plymouth', founded=1928, HQ=u'Auburn Hills, Michigan', disc=2001>
<id=15, name=u'Tesla', founded=2003, HQ=u'Palo Alto, CA', disc=None>


# Get all models with names that begin with "Cor".

>>> cor_models = Model.query.filter(Model.name.like('Cor%')).all()

>>> for model in cor_models:
...     print model
...
<id=5, year=1953, brand_name=u'Chevrolet', name=u'Corvette'>
<id=6, year=1954, brand_name=u'Chevrolet', name=u'Corvette'>
<id=8, year=1955, brand_name=u'Chevrolet', name=u'Corvette'>
<id=10, year=1956, brand_name=u'Chevrolet', name=u'Corvette'>
<id=11, year=1957, brand_name=u'Chevrolet', name=u'Corvette'>
<id=13, year=1958, brand_name=u'Chevrolet', name=u'Corvette'>
<id=17, year=1959, brand_name=u'Chevrolet', name=u'Corvette'>
<id=19, year=1960, brand_name=u'Chevrolet', name=u'Corvair'>
<id=20, year=1960, brand_name=u'Chevrolet', name=u'Corvette'>
<id=26, year=1961, brand_name=u'Chevrolet', name=u'Corvette'>
<id=28, year=1962, brand_name=u'Chevrolet', name=u'Corvette'>
<id=37, year=1963, brand_name=u'Chevrolet', name=u'Corvair 500'>
<id=38, year=1963, brand_name=u'Chevrolet', name=u'Corvette'>
<id=39, year=1964, brand_name=u'Chevrolet', name=u'Corvette'>


# Get all brands with that were founded in 1903 and that are not yet discontinued.

>>> brands = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

>>> for brand in brands:
...     print brand
...
<id=1, name=u'Ford', founded=1903, HQ=u'Dearborn, MI', disc=None>
<id=12, name=u'Buick', founded=1903, HQ=u'Detroit, MI', disc=None>


# Get all brands with that are either discontinued or founded before 1950.

>>> brands = Brand.query.filter( db.or_(Brand.discontinued != None, Brand.founded < 1950) )

>>> for brand in brands:
...     print brand
...

<id=1, name=u'Ford', founded=1903, HQ=u'Dearborn, MI', disc=None>
<id=2, name=u'Chrysler', founded=1925, HQ=u'Auburn Hills, Michigan', disc=None>
<id=3, name=u'Citro\xebn', founded=1919, HQ=u'Saint-Ouen, France', disc=None>
<id=4, name=u'Hillman', founded=1907, HQ=u'Ryton-on-Dunsmore, England', disc=1981>
<id=5, name=u'Chevrolet', founded=1911, HQ=u'Detroit, Michigan', disc=None>
<id=6, name=u'Cadillac', founded=1902, HQ=u'New York City, NY', disc=None>
<id=7, name=u'BMW', founded=1916, HQ=u'Munich, Bavaria, Germany', disc=None>
<id=8, name=u'Austin', founded=1905, HQ=u'Longbridge, England', disc=1987>
<id=9, name=u'Fairthorpe', founded=1954, HQ=u'Chalfont St Peter, Buckinghamshire', disc=1976>
<id=10, name=u'Studebaker', founded=1852, HQ=u'South Bend, Indiana', disc=1967>
<id=11, name=u'Pontiac', founded=1926, HQ=u'Detroit, MI', disc=2010>
<id=12, name=u'Buick', founded=1903, HQ=u'Detroit, MI', disc=None>
<id=13, name=u'Rambler', founded=1901, HQ=u'Kenosha, Washington', disc=1969>
<id=14, name=u'Plymouth', founded=1928, HQ=u'Auburn Hills, Michigan', disc=2001>


# Get any model whose brand_name is not Chevrolet.

>>> models = Model.query.filter(Model.brand_name != 'Chevrolet')

>>> for model in models:
...     print model
...
<id=1, year=1909, brand_name=u'Ford', name=u'Model T'>
<id=2, year=1926, brand_name=u'Chrysler', name=u'Imperial'>
<id=3, year=1948, brand_name=u'Citro\xebn', name=u'2CV'>
<id=4, year=1950, brand_name=u'Hillman', name=u'Minx Magnificent'>
<id=7, year=1954, brand_name=u'Cadillac', name=u'Fleetwood'>
<id=9, year=1955, brand_name=u'Ford', name=u'Thunderbird'>
<id=12, year=1957, brand_name=u'BMW', name=u'600'>
<id=14, year=1958, brand_name=u'BMW', name=u'600'>
<id=15, year=1958, brand_name=u'Ford', name=u'Thunderbird'>
<id=16, year=1959, brand_name=u'Austin', name=u'Mini'>
<id=18, year=1959, brand_name=u'BMW', name=u'600'>
<id=21, year=1960, brand_name=u'Fillmore', name=u'Fillmore'>
<id=22, year=1960, brand_name=u'Fairthorpe', name=u'Rockette'>
<id=23, year=1961, brand_name=u'Austin', name=u'Mini Cooper'>
<id=24, year=1961, brand_name=u'Studebaker', name=u'Avanti'>
<id=25, year=1961, brand_name=u'Pontiac', name=u'Tempest'>
<id=27, year=1962, brand_name=u'Pontiac', name=u'Grand Prix'>
<id=29, year=1962, brand_name=u'Studebaker', name=u'Avanti'>
<id=30, year=1962, brand_name=u'Buick', name=u'Special'>
<id=31, year=1963, brand_name=u'Austin', name=u'Mini'>
<id=32, year=1963, brand_name=u'Austin', name=u'Mini Cooper S'>
<id=33, year=1963, brand_name=u'Rambler', name=u'Classic'>
<id=34, year=1963, brand_name=u'Ford', name=u'E-Series'>
<id=35, year=1963, brand_name=u'Studebaker', name=u'Avanti'>
<id=36, year=1963, brand_name=u'Pontiac', name=u'Grand Prix'>
<id=40, year=1964, brand_name=u'Ford', name=u'Mustang'>
<id=41, year=1964, brand_name=u'Ford', name=u'Galaxie'>
<id=42, year=1964, brand_name=u'Pontiac', name=u'GTO'>
<id=43, year=1964, brand_name=u'Pontiac', name=u'LeMans'>
<id=44, year=1964, brand_name=u'Pontiac', name=u'Bonneville'>
<id=45, year=1964, brand_name=u'Pontiac', name=u'Grand Prix'>
<id=46, year=1964, brand_name=u'Plymouth', name=u'Fury'>
<id=47, year=1964, brand_name=u'Studebaker', name=u'Avanti'>
<id=48, year=1964, brand_name=u'Austin', name=u'Mini Cooper'>


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
