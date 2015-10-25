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

brand = Brand.query.get(8)
print "\n**Brand with ID 8:"
print brand


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

models = Model.query.filter(Model.name == 'Corvette',
                            Model.brand_name == 'Chevrolet').all()

print "\n**Models with name Corvette and brand Chevrolet:"
for model in models:
    print model


# Get all models that are older than 1960.

old_models = Model.query.filter(Model.year < 1960).all()

print "\n**Models older than 1960:"
for model in old_models:
    print model


# Get all brands that were founded after 1920.

youngbrands = Brand.query.filter(Brand.founded > 1920).all()

print "\n**Brands founded after 1920:"
for brand in youngbrands:
    print brand


# Get all models with names that begin with "Cor".

cor_models = Model.query.filter(Model.name.like('Cor%')).all()

print "\n**Models with names that begin with \"Cor\":"
for model in cor_models:
    print model

# Get all brands with that were founded in 1903 and that are not yet discontinued.

brands = Brand.query.filter(Brand.founded == 1903,
                            Brand.discontinued == None).all()

print "\n**Brands founded in 1903 and not yet discontinued"
for brand in brands:
    print brand


# Get all brands with that are either discontinued or founded before 1950.

brands = Brand.query.filter( db.or_(Brand.discontinued != None,
                                    Brand.founded < 1950) )

print "\n**Brands that are either discontinued or founded before 1950:"
for brand in brands:
    print brand


# Get any model whose brand_name is not Chevrolet.

models = Model.query.filter(Model.brand_name != 'Chevrolet')

print "\n**Models that are not a Chevrolet:"
for model in models:
    print model


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()

    for model in models:
        print "Model: %s, Brand: %s, HQ: %s" % (model.name, model.brand_name,
                                                model.brand.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()

    for brand in brands:
        print "BRAND: %s" % brand.name.upper()
        for model in brand.models:
            print "%s, %d" % (model.name, model.year)
        print "\n"


print "\n**Model, brand, and brand headquarters for 1964 models:"
get_model_info(1964)

print "\n**Brands Summary"
get_brands_summary()

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Design a function in python that takes in any string as parameter,
    and returns a list of objects that are brands whose name contains or is
    equal to the input string."""

    brands = Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()
    return brands


def get_models_between(start_year, end_year):
    """Design a function that takes in a start year and end year (two
    integers),and returns a list of objects that are models with years
    that fall between the start year and end year"""

    years = []
    current_year = start_year + 1

    for yr in range(end_year - start_year - 1):
        years.append(current_year)
        current_year += 1

    models = Model.query.filter(Model.year.in_(years)).all()

    return models

print "\n**Search for brand names with \"Ch\" in the name:"
brands = search_brands_by_name('Ch')

for brand in brands:
    print brand

print "\n**Get models made between 1960 and 1963:"
print "(This means start_year = 1959 and end_year = 1964)"
models = get_models_between(1959, 1964)

for model in models:
    print model

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# Returned value is a list of the one Brand object with the name Ford.



# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is used to linke a many-to-many relationship between
# two tables. With an association table, you give yourself flexibility to make
# changes in one table while minimizing the effect of the change on its "many-to-
# many" partner table. You also avoid problems associated with having fields that
# might have multiple values.
