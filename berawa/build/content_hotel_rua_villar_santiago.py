# Contenido de la demo Hotel Rúa Villar (Santiago de Compostela) (es/ca/en/fr). Hechos de hotelruavillar.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Individual','Doble estándar','Doble superior'],'ca':['Individual','Doble estàndard','Doble superior'],'en':['Single','Standard double','Superior double'],'fr':['Individuelle','Double standard','Double supérieure']}
RD={
'es':['Cálida estancia con cama matrimonial, completamente equipada, para viajar en soledad.','Con cama matrimonial o dos camas, suelo de madera y un diseño interior acogedor.','Muy amplia y luminosa, con balcón y/o galería con vistas a la rúa do Vilar, cama «king size» y sofá.'],
'ca':['Estada càlida amb llit de matrimoni, completament equipada, per viatjar en solitari.','Amb llit de matrimoni o dos llits, terra de fusta i un disseny interior acollidor.','Molt àmplia i lluminosa, amb balcó i/o galeria amb vistes a la rúa do Vilar, llit «king size» i sofà.'],
'en':['A warm stay with a double bed, fully equipped, for travelling alone.','With a double bed or two beds, wooden floor and a cosy interior design.','Very spacious and bright, with a balcony and/or gallery overlooking rúa do Vilar, a king-size bed and a sofa.'],
'fr':['Séjour chaleureux avec lit double, entièrement équipée, pour voyager seul.','Avec lit double ou deux lits, parquet en bois et décoration intérieure accueillante.','Très spacieuse et lumineuse, avec balcon et/ou galerie donnant sur la rúa do Vilar, lit king size et canapé.']}
ART={
'hero':('arches',9501,['#e6e4dc','#c9bfa3','#8f7a47','#4c5a52','#2a342f']),
'intro':('columns',9502,['#e9e6dc','#f2eee0','#b9853a','#586a60','#2a342f']),
'r1':('arches',9511,['#e5e3da','#c8bea2','#8c7743','#48564e','#27312c']),
'r2':('columns',9512,['#e4e2d8','#f0ecdd','#b58238','#546459','#29332e']),
'r3':('skyline',9513,['#33443f','#e8935f','#fbd9a0','#32423d','#26332f','#19231f']),
'g1':('arches',9521,['#e7e5dc','#cac0a5','#917c49','#4d5b53','#2b352f']),
'g2':('skyline',9522,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g3':('columns',9523,['#e5e3d9','#f1ede0','#bb873c','#5a6c62','#2d3832']),
'g4':('hills',9524,['#e6e6d1','#f3e5c3','#f6cf8a','#a9c19e','#80a085','#587767']),
'g5':('arches',9525,['#e6e4db','#c7bda1','#8e7945','#4a584f','#28322d']),
'g6':('skyline',9526,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Rúa Villar · Hotel con encanto a 15 metros de la Catedral de Santiago',see_rooms='Ver habitaciones',hero_k='Santiago de Compostela · Rúa do Vilar',hero_t='Un hotel con encanto junto a la Catedral',hero_s='Una antigua casa señorial del siglo XVIII con 17 habitaciones, a 15 metros de la Catedral de Santiago.',
 intro_t='Una casa señorial convertida en hotel',intro_p1='El Hotel Rúa Villar ocupa una casa señorial del siglo XVIII restaurada, en la rúa do Vilar 8-10, con 17 habitaciones.',
 intro_p2='Tiene desayuno bufé, recepción 24 horas, salón social con chimenea y ascensor panorámico. Para reservar, contacta con el hotel por teléfono o correo.',
 stats=['17 habitaciones','A 15 m de la Catedral','Recepción 24 horas','Ascensor panorámico'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Tres de los tipos de habitación del hotel.',
 svcs=['Desayuno bufé','Recepción 24 horas','Wifi gratuito','Ascensor panorámico','Servicio de habitaciones','Espacio para guardar el equipaje','Servicio de lavandería','Salón social con chimenea'],
 loc_p='Rúa do Vilar 8-10, 15705 Santiago de Compostela.',
 chips=['¿Cuántas habitaciones tiene?','¿Hay parking?','¿Dónde está?','¿Cómo se reserva?']),
'ca':dict(title='Hotel Rúa Villar · Hotel amb encant a 15 metres de la Catedral de Santiago',see_rooms='Veure habitacions',hero_k='Santiago de Compostela · Rúa do Vilar',hero_t='Un hotel amb encant al costat de la Catedral',hero_s='Una antiga casa senyorial del segle XVIII amb 17 habitacions, a 15 metres de la Catedral de Santiago.',
 intro_t='Una casa senyorial convertida en hotel',intro_p1='L\'Hotel Rúa Villar ocupa una casa senyorial del segle XVIII restaurada, a la rúa do Vilar 8-10, amb 17 habitacions.',
 intro_p2='Té esmorzar bufet, recepció 24 hores, saló social amb xemeneia i ascensor panoràmic. Per reservar, contacta amb l\'hotel per telèfon o correu.',
 stats=['17 habitacions','A 15 m de la Catedral','Recepció 24 hores','Ascensor panoràmic'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Tres dels tipus d\'habitació de l\'hotel.',
 svcs=['Esmorzar bufet','Recepció 24 hores','Wifi gratuïta','Ascensor panoràmic','Servei d\'habitacions','Espai per guardar l\'equipatge','Servei de bugaderia','Saló social amb xemeneia'],
 loc_p='Rúa do Vilar 8-10, 15705 Santiago de Compostela.',
 chips=['Quantes habitacions té?','Hi ha pàrquing?','On és?','Com es reserva?']),
'en':dict(title='Hotel Rúa Villar · Charming hotel 15 metres from Santiago Cathedral',see_rooms='See the rooms',hero_k='Santiago de Compostela · Rúa do Vilar',hero_t='A charming hotel next to the Cathedral',hero_s='A former 18th-century manor house with 17 rooms, 15 metres from Santiago Cathedral.',
 intro_t='A manor house turned hotel',intro_p1='Hotel Rúa Villar occupies a restored 18th-century manor house at rúa do Vilar 8-10, with 17 rooms.',
 intro_p2='It has a buffet breakfast, a 24-hour reception, a lounge with a fireplace and a panoramic lift. To book, contact the hotel by phone or email.',
 stats=['17 rooms','15 m from the Cathedral','24-hour reception','Panoramic lift'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Three of the hotel\'s room types.',
 svcs=['Buffet breakfast','24-hour reception','Free wifi','Panoramic lift','Room service','Luggage storage','Laundry service','Lounge with fireplace'],
 loc_p='Rúa do Vilar 8-10, 15705 Santiago de Compostela.',
 chips=['How many rooms does it have?','Is there parking?','Where is it?','How do I book?']),
'fr':dict(title='Hotel Rúa Villar · Hôtel de charme à 15 mètres de la cathédrale de Saint-Jacques',see_rooms='Voir les chambres',hero_k='Saint-Jacques-de-Compostelle · Rúa do Vilar',hero_t='Un hôtel de charme à côté de la cathédrale',hero_s='Une ancienne demeure seigneuriale du XVIIIe siècle avec 17 chambres, à 15 mètres de la cathédrale.',
 intro_t='Une demeure seigneuriale devenue hôtel',intro_p1='L\'Hotel Rúa Villar occupe une demeure seigneuriale du XVIIIe siècle restaurée, rúa do Vilar 8-10, avec 17 chambres.',
 intro_p2='Il propose petit-déjeuner buffet, réception 24 heures, salon avec cheminée et ascenseur panoramique. Pour réserver, contactez l\'hôtel par téléphone ou e-mail.',
 stats=['17 chambres','À 15 m de la cathédrale','Réception 24 heures','Ascenseur panoramique'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Trois des types de chambre de l\'hôtel.',
 svcs=['Petit-déjeuner buffet','Réception 24 heures','Wifi gratuit','Ascenseur panoramique','Service en chambre','Consigne à bagages','Service de blanchisserie','Salon avec cheminée'],
 loc_p='Rúa do Vilar 8-10, 15705 Saint-Jacques-de-Compostelle.',
 chips=['Combien de chambres a-t-il ?','Y a-t-il un parking ?','Où est-il ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@hotelruavillar.com')
D=dict(name='Hotel Rúa Villar',ac='#3b4a43',ac2='#b9853a',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Rúa do Vilar 8-10 · 15705 Santiago de Compostela',phones=['981 51 98 58'],emails=['info@hotelruavillar.com'],maps='Hotel Rúa Villar, Rúa do Vilar 8-10, Santiago de Compostela',t=T)
META=dict(repo='demo-hotel-rua-villar-santiago',name='Hotel Rúa Villar',legal_name='Rúa Villar Restauración S.L.',registry_ids=['CIF B82465527'],
 url='https://hotelruavillar.com/',domain='hotelruavillar.com',municipality='Santiago de Compostela',province='A Coruña',sector='hotel con encanto en una casa señorial',
 read_at='2026-10-29T06:15:00+01:00',created_at='2026-10-29T06:16:00+01:00',built_at='2026-10-29T06:16:00+01:00',audit_date='2026-10-29T06:16:00+01:00',
 rating=dict(value=4.7,coincide=['telefono','web'],date='2026-10-29T06:13:31+01:00',url='https://www.google.com/maps/place/Hotel+Rua+Villar/@42.8794904,-8.544314,17z/data=!4m9!3m8!1s0xd2efe46ac123829:0xbfc6d20a007f4d1d!5m2!4m1!1i2!8m2!3d42.8794904!4d-8.544314!16s%2Fg%2F1tddz1fl'),
 book=dict(mode='mail',email='info@hotelruavillar.com',note='La web del negocio tiene su propio motor de reservas cuyo enlace no se verifica; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel con precedente en demos de esta tanda')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿Qué equipamiento tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Hay parking?','K04'),('¿Dónde está el hotel?','K05'),('¿Qué historia tiene el edificio?','K06'),('¿Cómo reservo?','K07'),('¿Cuál es el teléfono?','K08'),('¿Quién es el titular?','K09'),('¿Hay ascensor?','K02'),('¿Hay servicio de lavandería?','K03'),('¿Admiten mascotas?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K07'),('¿Tienen suites?',None),('¿Hay piscina?',None)],
'ca':[('Quantes habitacions té?','K01'),('Quin equipament tenen les habitacions?','K02'),('Hi ha esmorzar?','K03'),('Hi ha pàrquing?','K04'),('On és l\'hotel?','K05'),('Quina història té l\'edifici?','K06'),('Com reservo?','K07'),('Quin és el telèfon?','K08'),('Qui és el titular?','K09'),('Hi ha ascensor?','K02'),('Hi ha servei de bugaderia?','K03'),('Admeteu mascotes?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K07'),('Teniu suites?',None),('Hi ha piscina?',None)],
'en':[('How many rooms does it have?','K01'),('What equipment do the rooms have?','K02'),('Is there breakfast?','K03'),('Is there parking?','K04'),('Where is the hotel?','K05'),('What history does the building have?','K06'),('How do I book?','K07'),('What is the phone number?','K08'),('Who is the owner?','K09'),('Is there a lift?','K02'),('Is there a laundry service?','K03'),('Are pets allowed?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K07'),('Do you have suites?',None),('Is there a swimming pool?',None)],
'fr':[('Combien de chambres a-t-il ?','K01'),('Quel équipement ont les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Y a-t-il un parking ?','K04'),('Où est l\'hôtel ?','K05'),('Quelle histoire a le bâtiment ?','K06'),('Comment réserver ?','K07'),('Quel est le téléphone ?','K08'),('Qui est le titulaire ?','K09'),('Y a-t-il un ascenseur ?','K02'),('Y a-t-il un service de blanchisserie ?','K03'),('Les animaux sont-ils admis ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K07'),('Avez-vous des suites ?',None),('Y a-t-il une piscine ?',None)]}
