CREATE TABLE type_kofee (
    type_id INT PRIMARY KEY,
    title TEXT
);


CREATE TABLE kofee (
    kofee_id INT PRIMARY KEY,
    name_kof TExt NOT NULL
    koeff INT NOT NULL,
    opis_vkus TEXT NOT NULL,
    price INT NOT NULL,
    volume INT NOT NULL,
    kof_id INT NOT NULL,
    FOREIGN KEY (type_id) 
      REFERENCES type_kofee(type_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);

INSERT INTO type_kofee(type_id, title) VALUES(1, 'молотый');
INSERT INTO type_kofee(type_id, title) VALUES(2, 'в зернах');
INSERT INTO kofee(kofee_id, name_kof, koeff, opis_vkus, price, volume, kof_id) VALUES(1, 'душистый', 10, 'рекомендует ди каприо', 150, 30, 1);
INSERT INTO kofee(kofee_id, name_kof, koeff, opis_vkus, price, volume, kof_id) VALUES(2, 'жоский', 100, 'очень горький', 300, 30, 2);


