USE biusratdb;

SELECT * FROM api_programa;
INSERT INTO api_programa(id, nombre_programa, descrip_programa)
VALUES (1, "Programa de perdida de grasa", "Este programa combina entrenamiento cardiovascular con ejercicios de fuerza para maximizar la quema de calorías y mantener el metabolismo activo. Además, se enfoca en la alimentación saludable y el control de las porciones para crear un déficit calórico."),
(2, "Programa de Recomposición Corporal","Este programa se centra en la combinación de entrenamiento de fuerza progresivo y una dieta balanceada para mejorar la definición muscular y reducir la grasa corporal."),
(3, "Programa de aumento de masa muscular","Este programa se enfoca en el entrenamiento de fuerza progresivo con un énfasis en el levantamiento de pesas y la hipertrofia muscular.");

SELECT * FROM api_ejercicio;
SELECT * FROM api_entrenamiento;
SELECT * FROM api_alimentacion;
SELECT * FROM api_comida;

INSERT INTO api_entrenamiento(id,tipo_entrenamiento,dificultad,id_programa_id)
VALUES (1,"TREN SUPERIROR","PRINCIPIANTE",1),
(2, "TREN INFERIOR", "PRINCIPIANTE", 1),
(3, "CUERPO COMPLETO", "PRINCIPIANTE", 1),
(4, "CARDIO HIIT", "PRINCIPIANTE", 1),
(5,"TREN SUPERIROR","INTERMEDIO",2),
(6, "TREN INFERIOR", "INTERMEDIO", 2),
(7, "CUERPO COMPLETO", "INTERMEDIO", 2),
(8, "CARDIO HIIT", "INTERMEDIO", 2),
(9,"TREN SUPERIROR","AVANZADO",3),
(10, "TREN INFERIOR", "AVANZADO", 3),
(11, "CUERPO COMPLETO", "AVANZADO", 3),
(12, "CARDIO HIIT", "AVANZADO", 3);

INSERT INTO api_ejercicio(id, nombre_ejercicio, descrip_ejercicio, serie,repeticion,peso,id_entrenamiento_id)
VALUES (1, "PRESS BANCA", "Trabaja el pecho, hombros y tríceps.", 4, 12, "LIVIANO - MODERADO", 1),
(2, "PRESS MILITAR", "Trabaja los hombros y tríceps.", 4, 12, "LIVIANO - MODERADO", 1),
(3, "FONDOS", "Trabaja el pecho, hombros y tríceps.", 4, 12, "LIVIANO - MODERADO", 1),
(4, "DOMINADAS", "Trabaja la espalda y bíceps.", 4, 12, "LIVIANO - MODERADO", 1),
(5, "SENTADILLA", "Trabaja los músculos de las piernas y glúteos.", 4, 12, "LIVIANO - MODERADO", 2),
(6, "HIPTRHUST", "Trabaja los glúteos y parte baja de la espalda.", 4, 12, "LIVIANO - MODERADO", 2),
(7, "PESO MUERTO RUMANO", "Trabaja los glúteos, isquiotibiales y la parte baja de la espalda.", 4, 12, "LIVIANO - MODERADO", 2),
(8, "ABDUCTOR", "Trabaja los músculos abductores de las piernas.", 4, 12, "LIVIANO - MODERADO", 2),
(9, "PRESS BANCA", "Trabaja el pecho, hombros y tríceps.", 4, 12, "LIVIANO - MODERADO", 3),
(10, "PESO MUERTO", "Trabaja la espalda baja, glúteos y piernas.", 4, 12, "LIVIANO - MODERADO", 3),
(11, "SENTADILLA", "Trabaja los músculos de las piernas y glúteos.", 4, 12, "LIVIANO - MODERADO", 3),
(12, "HIPTRHUST", "Trabaja los glúteos y parte baja de la espalda.", 4, 12, "LIVIANO - MODERADO", 3),
(13, "Burpees", "Ejercicio cardiovascular de cuerpo completo.", 4, 12, "Peso corporal", 4),
(14, "Escaladores", "Ejercicio cardiovascular de cuerpo completo.", 4, 12, "Peso corporal", 4),
(15, "Jumping jacks", "Ejercicio cardiovascular de cuerpo completo.", 4, 12, "Peso corporal", 4),
(16, "Plancha Abdominal", "Trabaja el core.", 4, 12, "Peso corporal", 4),
(17,"PRESS BANCA", "Trabaja el pecho, hombros y tríceps.",5,8,"MODERADO",5),
(18,"PRESS MILITAR", "Trabaja los hombros y tríceps.",5,8,"MODERADO",5),
(19, "FONDOS", "Trabaja el pecho, hombros y tríceps.",5,8,"MODERADO",5),
(20,"DOMINADAS", "Trabaja la espalda y bíceps.",5,8,"MODERADO",5),
(21,"SENTADILLA", "Trabaja los músculos de las piernas y glúteos.",5,8,"MODERADO",6),
(22,"HIPTRHUST", "Trabaja los glúteos y parte baja de la espalda.",5,8,"MODERADO",6),
(23,"PESO MUERTO RUMANO", "Trabaja los glúteos, isquiotibiales y la parte baja de la espalda.",5,8,"MODERADO",6),
(24,"ABDUCTOR", "Trabaja los músculos abductores de las piernas.",5,8,"MODERADO",6),
(25,"PRESS BANCA", "Trabaja el pecho, hombros y tríceps.",5,8,"MODERADO",7),
(26,"PESO MUERTO", "Trabaja la espalda baja, glúteos y piernas.",5,8,"MODERADO",7),
(27,"SENTADILLA", "Trabaja los músculos de las piernas y glúteos.",5,8,"MODERADO",7),
(28,"HIPTRHUST", "Trabaja los glúteos y parte baja de la espalda.",5,8,"MODERADO",7),
(29,"Burpees", "Ejercicio cardiovascular de cuerpo completo.",5,8,"MODERADO",8),
(30,"Escaladores", "Ejercicio cardiovascular de cuerpo completo.",5,8,"MODERADO",8),
(31,"Jumping jacks", "Ejercicio cardiovascular de cuerpo completo.",5,8,"MODERADO",8),
(32,"Plancha Abdominal", "Trabaja el core.",5,8,"MODERADO",8),
(33, "PRESS BANCA", "Trabaja el pecho, hombros y tríceps.",5,5,"PESADO",9),
(34,"PRESS MILITAR", "Trabaja los hombros y tríceps.",5,5,"PESADO",9),
(35,"FONDOS", "Trabaja el pecho, hombros y tríceps.",5,5,"PESADO",9),
(36,"DOMINADAS", "Trabaja la espalda y bíceps.",5,5,"PESADO",9),
(37,"SENTADILLA", "Trabaja los músculos de las piernas y glúteos.",5,5,"PESADO",10),
(38,"HIPTRHUST", "Trabaja los glúteos y parte baja de la espalda.",5,5,"PESADO",10),
(39,"PESO MUERTO RUMANO", "Trabaja los glúteos, isquiotibiales y la parte baja de la espalda.",5,5,"PESADO",10),
(40,"ABDUCTOR", "Trabaja los músculos abductores de las piernas.",5,5,"PESADO",10),
(41,"PRESS BANCA", "Trabaja el pecho, hombros y tríceps.",5,5,"PESADO",11),
(42,"PESO MUERTO", "Trabaja la espalda baja, glúteos y piernas.",5,5,"PESADO",11),
(43,"SENTADILLA", "Trabaja los músculos de las piernas y glúteos.",5,5,"PESADO",11),
(44,"HIPTRHUST", "Trabaja los glúteos y parte baja de la espalda.",5,5,"PESADO",11),
(45,"Burpees", "Ejercicio cardiovascular de cuerpo completo.",5,5,"PESADO",12),
(46,"Escaladores", "Ejercicio cardiovascular de cuerpo completo.",5,5,"PESADO",12),
(47,"Jumping jacks", "Ejercicio cardiovascular de cuerpo completo.",5,5,"PESADO",12),
(48,"Plancha Abdominal", "Trabaja el core.",5,5,"PESADO",12);

INSERT INTO api_alimentacion(id,comida_tiempo,id_programa_id)
VALUES (1, "DESAYUNO", 1),
(2, "ALMUERZO", 1),
(3, "CENA", 1),
(4, "DESAYUNO", 2),
(5, "ALMUERZO", 2),
(6, "CENA", 2),
(7, "DESAYUNO", 3),
(8, "ALMUERZO", 3),
(9, "CENA", 3);

INSERT INTO api_comida(id,nombre_plato, calorias, cant_proteinas, cant_grasas, cant_carbo,id_alimentacion_id)
VALUES (1, "Revuelto de claras de huevo con espinacas", 150, 10,5,0, 1),
(2, "Ensalada de pollo a la parrilla con verduras mixtas", 300, 20,15,10, 2),
(3, "Salmón al horno con brócoli al vapor", 400, 25,20,15, 3),
(4, "Batido de proteínas con plátano y avena", 300, 25,8,30, 4),
(5, "Pechuga de pollo a la parrilla con arroz integral y vegetales al vapor", 400, 30,10,40, 5),
(6, "Filete de salmón a la plancha con quinoa y espárragos asados", 450, 35,15,35, 6),
(7, "Tortilla de huevos con espinacas y aguacate", 400, 25,20,10, 7),
(8, "Pechuga de pollo a la parrilla con batata asada y brócoli al vapor", 450, 30,15,40, 8),
(9, "Filete de ternera a la plancha con patatas horneadas y espárragos a la parrilla", 500, 35,25,30, 9);

INSERT INTO api_todaymeal (name, image, time) VALUES
('Salmon Nigiri', 'assets/images/m_1.png', '2024-03-28 07:00:00'),
('Leche Baja en calorias', 'assets/images/m_2.png', '2024-03-28 08:00:00');
INSERT INTO api_findeat (name, image, number) VALUES
('Desayuno', 'assets/images/m_3.png', '120+ Comidas'),
('Almuerzo', 'assets/images/m_4.png', '130+ Comidas');
INSERT INTO api_popular (name, image, b_image, size, time, kcal) VALUES
('Blueberry Pancake', 'assets/images/f_1.png', 'assets/images/pancake_1.png', 'Mediano', '30mins', '230kCal'),
('Salmon Nigiri', 'assets/images/f_2.png', 'assets/images/nigiri.png', 'Mediano', '20mins', '120kCal');
INSERT INTO api_recomendado (name, image, size, time, kcal) VALUES
('Pancakes con miel', 'assets/images/rd_1.png', 'Facil', '30mins', '180kCal'),
('Pan rollo', 'assets/images/m_4.png', 'Facil', '20mins', '230kCal');
INSERT INTO api_categoria (name, image) VALUES
('Ensalada', 'assets/images/c_1.png'),
('Pastel', 'assets/images/c_2.png'),
('Pie', 'assets/images/c_3.png'),
('Smoothies', 'assets/images/c_4.png'),
('Ensalada', 'assets/images/c_1.png'),
('Pastel', 'assets/images/c_2.png'),
('Pie', 'assets/images/c_3.png'),
('Smoothies', 'assets/images/c_4.png');
INSERT INTO api_desayuno (name, time, image) VALUES
('Pancakes con miel', '07:00am', 'assets/images/honey_pan.png'),
('Cafe', '07:30am', 'assets/images/coffee.png');
INSERT INTO api_almuerzo (name, time, image) VALUES
('Presa de pollo', '01:00pm', 'assets/images/chicken.png'),
('Leche', '01:20pm', 'assets/images/glass-of-milk 1.png');
INSERT INTO api_snack (name, time, image) VALUES
('Naranja', '04:30pm', 'assets/images/orange.png'),
('Pie de manzana', '04:40pm', 'assets/images/apple_pie.png');
INSERT INTO api_cena (name, time, image) VALUES
('Ensalada', '07:10pm', 'assets/images/salad.png'),
('Avena', '08:10pm', 'assets/images/oatmeal.png');
INSERT INTO api_nutricion (title, image, unit_name, value, max_value) VALUES
('Calories', 'assets/images/burn.png', 'kCal', '350', '500'),
('Proteinas', 'assets/images/proteins.png', 'g', '300', '1000'),
('Grasas', 'assets/images/egg.png', 'g', '140', '1000'),
('Carbo', 'assets/images/carbo.png', 'g', '140', '1000');
INSERT INTO api_nutrition (image, title) VALUES
('assets/images/burn.png', '180kCal'),
('assets/images/egg.png', '30g grasas'),
('assets/images/proteins.png', '20g proteinas'),
('assets/images/carbo.png', '50g carbo');
INSERT INTO api_ingredientes (image, title, value) VALUES
('assets/images/flour.png', 'Harina de trigo', '100grm'),
('assets/images/sugar.png', 'Sugar', '3 tbsp'),
('assets/images/baking_soda.png', 'Bicarbonato', '2tsp'),
('assets/images/eggs.png', 'Huevos', '2 items');
INSERT INTO api_paso (no, detail) VALUES
('1', 'Prepara todos los ingredientes que necesites'),
('2', 'Mezcla harina,azucar, sal y polvo para hornear'),
('3', 'En un lugar aparte, mezcle los huevos y la leche líquida hasta que se mezclen.'),
('4', 'Coloque la mezcla de huevo y leche en los ingredientes secos, revuelva hasta que quede suave y homogéneo.'),
('5', 'Prepare todos los ingredientes que necesite');
INSERT INTO api_hoysleep (name, image, time, duration)
VALUES
('Hora de dormir', 'assets/images/bed.png', '2023-06-01 21:00:00', 'en 6houras 22minutos'),
('Alarma', 'assets/images/alaarm.png', '2023-06-02 05:10:00', 'en 14houras 30minutos');
INSERT INTO api_evento (name, start_time)
VALUES
('Entrenamiento de abdominales', '2023-05-25 07:30:00'),
('Entrenamiento de la parte superior del cuerpo', '2023-05-25 09:00:00'),
('Entrenamiento de la parte inferior del cuerpo', '2023-05-25 15:00:00'),
('Entrenamiento de abdominales', '2023-05-26 07:30:00'),
('Entrenamiento de la parte superior del cuerpo', '2023-05-26 09:00:00'),
('Entrenamiento de la parte inferior del cuerpo', '2023-05-26 15:00:00'),
('Entrenamiento de abdominales', '2023-05-27 07:30:00'),
('Entrenamiento de la parte superior del cuerpo', '2023-05-27 09:00:00'),
('Entrenamiento de la parte inferior del cuerpo', '2023-05-27 15:00:00');
INSERT INTO api_latest (image, title, time) VALUES
('assets/images/Workout1.png', 'Fullbody Workout', 'Today, 03:00pm'),
('assets/images/Workout2.png', 'Upperbody Workout', 'June 05, 02:00pm');
INSERT INTO api_you (image, title) VALUES
('assets/images/barbell.png', 'Mancuerna'),
('assets/images/skipping_rope.png', 'Cuerda de Skipping'),
('assets/images/bottle.png', 'Botella de 1 litro');
INSERT INTO api_ejeset (name) VALUES
('Set 1'),
('Set 2');
INSERT INTO api_eje (exercise_set_id, image, title, value) VALUES
(1, 'assets/img/img_1.png', 'Calentamiento', '05:00'),
(1, 'assets/img/img_2.png', 'Jumping Jack', '12x'),
(1, 'assets/img/img_1.png', 'Saltar la cuerda', '15x'),
(1, 'assets/img/img_2.png', 'Sentadillas', '20x'),
(1, 'assets/img/img_1.png', 'Levantamiento de brazos', '00:53'),
(1, 'assets/img/img_2.png', 'Descanso y bebida', '02:00');

INSERT INTO api_eje  (exercise_set_id, image, title, value) VALUES
(2, 'assets/img/img_1.png', 'Calentamiento', '05:00'),
(2, 'assets/img/img_2.png', 'Jumping Jack', '12x'),
(2, 'assets/img/img_1.png', 'Saltar la cuerda', '15x'),
(2, 'assets/img/img_2.png', 'Sentadillas', '20x'),
(2, 'assets/img/img_1.png', 'Levantamiento de brazos', '00:53'),
(2, 'assets/img/img_2.png', 'Descanso y bebida', '02:00');