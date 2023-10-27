from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('drivers/', views.drivers, name='drivers'),
    path('driver/<int:pk>', views.driver_record, name='driver'),
    path('delete_driver/<int:pk>', views.delete_driver, name='delete_driver'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('update_driver/<int:pk>', views.update_driver, name='update_driver'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:pk>', views.car_record, name='car'),
    path('delete_car/<int:pk>', views.delete_car, name='delete_car'),
    path('add_car/', views.add_car, name='add_car'),
    path('update_car/<int:pk>', views.update_car, name='update_car'),
    path('vls/', views.vls, name='vls'),
    path('vl/<int:pk>', views.vl_record, name='vl'),
    path('delete_vl/<int:pk>', views.delete_vl, name='delete_vl'),
    path('add_vl/', views.add_vl, name='add_vl'),
    path('update_vl/<int:pk>', views.update_vl, name='update_vl'),
    path('fcards/', views.fcards, name='fcards'),
    path('fcard/<int:pk>', views.fcard_record, name='fcard'),
    path('delete_fcard/<int:pk>', views.delete_fcard, name='delete_fcard'),
    path('add_fcard/', views.add_fcard, name='add_fcard'),
    path('update_fcard/<int:pk>', views.update_fcard, name='update_fcard'),
    path('trips/', views.trips, name='trips'),
    path('trip/<int:pk>', views.trip_record, name='trip'),
    path('delete_trip/<int:pk>', views.delete_trip, name='delete_trip'),
    path('add_trip/', views.add_trip, name='add_trip'),
    path('update_trip/<int:pk>', views.update_trip, name='update_trip'),
    path('trips_csv', views.trips_csv, name='trips_csv'),
    path('dtrips_csv/<int:pk>', views.dtrips_csv, name='dtrips_csv'),
    path('ctrips_csv/<int:pk>', views.ctrips_csv, name='ctrips_csv'),
    path('vtrips_csv/<int:pk>', views.vtrips_csv, name='vtrips_csv'),

]