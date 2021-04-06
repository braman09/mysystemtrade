from datapackage import Package

# S and P 500 list

package = Package('https://datahub.io/core/s-and-p-500-companies/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())

# NASDAQ list

from datapackage import Package

package = Package('https://datahub.io/core/nasdaq-listings/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())

# VIX CBOE Volatility Index

from datapackage import Package

package = Package('https://datahub.io/core/finance-vix/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())


# NYSE listing

from datapackage import Package

package = Package('https://datahub.io/core/nyse-other-listings/datapackage.json')

# print list of all resources:
print(package.resource_names)

# print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())





        
