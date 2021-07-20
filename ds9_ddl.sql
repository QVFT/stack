CREATE TABLE farm
(
    farm_id int NOT NULL,
    description varchar(191),
    PRIMARY KEY (farm_id)
);

CREATE TABLE arduino
(
    arduino_id int NOT NULL,
    farm_id int NOT NULL,
    PRIMARY KEY (arduino_id),
    FOREIGN KEY (farm_id) REFERENCES farm(farm_id) ON DELETE cascade
);

CREATE TABLE collection(
    collection_id int NOT NULL,
    time DATE NOT NULL,
    PRIMARY KEY (collection_id)
);

CREATE TABLE supply_reading
(
    supply_id int NOT NULL,
    arduino_id int NOT NULL,
    collection_id int NOT NULL,
    excess_water int NOt NULL,
    nutrient_ed FLOAT(2) NOT NULL,
    water_ph FLOAT(2) NOT NULL,
    supply_pressure FLOAT(2) NOT NULL,
    supply_pump BOOLEAN,
    supply_3_way BOOLEAN,
    supply_sprinkler BOOLEAN,
    PRIMARY KEY (supply_id),
    FOREIGN KEY (arduino_id) REFERENCES arduino(arduino_id) ON DELETE cascade,
    FOREIGN KEY (collection_id) REFERENCES collection(collection_id) ON DELETE cascade

);

CREATE TABLE return_line
(
    return_id int NOT NULL,
    arduino_id int NOT NULL,
    collection_id int NOT NULL,
    farm_runoff_lvl FLOAT(2) NOT NULL,
    freshwater_lvl FLOAT(2) NOT NULL,
    return_pump BOOLEAN,
    return_3_way BOOLEAN,
    PRIMARY KEY (return_id),
    FOREIGN KEY (arduino_id) REFERENCES arduino(arduino_id) ON DELETE cascade,
    FOREIGN KEY (collection_id) REFERENCES collection(collection_id) ON DELETE cascade    
);

CREATE TABLE nutrient_zone
(
    nutrient_id int NOT NULL,
    arduino_id int NOT NULL,
    collection_id int NOT NULL,
    tank_ph_lvl FLOAT(2) NOT NULL,
    tank_A_lvl FLOAT(2) NOT NULL,
    tank_B_lvl FLOAT(2) NOT NULL,
    nutrient_pump BOOLEAN,
    PRIMARY KEY (nutrient_id),
    FOREIGN KEY (arduino_id) REFERENCES arduino(arduino_id) ON DELETE cascade,
    FOREIGN KEY (collection_id) REFERENCES collection(collection_id) ON DELETE cascade   
);

CREATE TABLE weight_sensor
(
    sensor_id int NOT NULL,
    PRIMARY KEY (sensor_id)
);

CREATE TABLE growth_zone(
    growth_id int NOT NULL,
    arduino_id int NOT NULL,
    collection_id int NOT NULL,
    sensor_id int NOT NULL,
    ambient_temp FLOAT(2) NOT NULL,
    webcam_live BOOLEAN NOT NULL,
    plant_weight FLOAT(2) NOT NULL,
    light_intensity_1 BOOLEAN,
    light_intensity_2 BOOLEAN,
    PRIMARY KEY (growth_id),
    FOREIGN KEY (arduino_id) REFERENCES arduino(arduino_id) ON DELETE cascade,
    FOREIGN KEY (collection_id) REFERENCES collection(collection_id) ON DELETE cascade,
    FOREIGN KEY (sensor_id) REFERENCES weight_sensor(sensor_id) ON DELETE cascade 

);
