from agency import agency
from bike import bike
from car import car
from client import client
from price_manager import price_manager
from rent import rent
from truck import truck


manager_test = price_manager()
v_test1 =bike("test_brand","test_model",2000,"test_plate",0,True,100,"test_type")
v_test2 =bike("test_brand","test_model",1984,"test_plate",0,False,100,"test_type")
v_test3 =car("test_brand","test_model",1999,"test_plate",0,True,3,"test_gas",50)
v_test4 =truck("test_brand","test_model",2001,"test_plate",0,True,500,1000,"test_license")
v_test5 =truck("test_brand","test_model",2012,"test_plate",0,False,500,1000,"test_license")
c_test1 =client("test","test","test_lincense","00/00/0000","test@test.test")
c_test2 =client("test2","test2","test_lincense","00/00/0000","test2@test.test")
c_test3 =client("test3","test3","test_lincense","00/00/0000","test3@test.test")
agency_test = agency("test",[v_test1,v_test2,v_test3,v_test4,v_test5],[],[],[c_test1,c_test2,c_test3])
agency_test.rent_vehicule(c_test1,v_test1,"00/00/0000")
agency_test.rent_vehicule(c_test2,v_test3,"00/00/0000")
agency_test.rent_vehicule(c_test3,v_test5,"00/00/0000")
print(str(agency_test._ongoing_rent))
agency_test.return_vehicule(agency_test._ongoing_rent[0],50,"00/00/0000")
agency_test.return_vehicule(agency_test._ongoing_rent[0],75,"00/00/0000")
agency_test.calculate_benefits()
manager_test.update_price("car",5)
print(str(manager_test._instance))
manager_test2 = price_manager()
print(str(manager_test2._instance))