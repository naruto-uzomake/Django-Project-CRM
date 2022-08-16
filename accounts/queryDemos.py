#***(1)Return all customer from customer table
customer = Customer.object.all()

#(2)Return first customer in table
firstCustomer = Customer.object.first()

#(3)Return last customer in table
lastCustomer = Customer.object.last()

#(4)Return single customer by name
customerByName = Customer.object.get(name='peter Piper')

#***(5)Return single customer by name
customerById = Customer.object.get(id=4)

#***(6)Return all order realted to customer (first customer variable set above)
firstCustomer.order_set.all()

#(7)***Return Orders Customer Name:(Query Parent Model vaues)
order = Order.object.first()
parentName = order.customer.name

#(8)***Return Product from prduct Table with the value of "Out Door" in category attribute
products = Product.object.filter(category="Out Door")

#(9)***Order/Sort Object by id
leastToGreatest = Product.object.all().order_by('id')
greatestToLeast = Product.object.all().order_by('-id')

#(10)***Return all product with tag of 'Sports":(Query Many To Many Fields)
productsFiltered = Product.object.filter(tags_name="Sports")

# ...
# # (11)Bonus
# # Q:If the customer has more than 1 ball, how would you reflect it in the database?
# # A:Beacuse there are many different products and this value change constantly you would most likly not want to
# # store the value in the database but rather just make this a function we can run each time we load the customer profile
# ...

# Return the total count for number of time a "Ball" was ordered by the first Customer
ballOrder = firstCustomer.order_set.filter(product_name= "Ball").count()

# Return total count for each product ordered
ballOrder = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1
# Returns: allOrders:{'Ball':2, 'BBQ Grill':1}

#RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    Parent = models.ForegnKey(parentModel)
    name = models.CharField(max_length=200, null=True)

    Parent = ParentModel.objects.first()
    parent.ChildModels.set.all()
