CREATE TABLE tbCafeList (
    idx INT AUTO_INCREMENT PRIMARY KEY, -- 자동 증가
    francise_name VARCHAR(255) NOT NULL, -- 최대 길이를 명시적으로 지정
    francise_addr VARCHAR(255) NOT NULL,
    francise_tel VARCHAR(255) NOT NULL,
    cafe_gubun INT NOT NULL CHECK (cafe_gubun IN (1, 2, 3)), -- CHECK 제약 조건
    regTime DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, -- 기본값으로 현재 시간
    regID VARCHAR(255) DEFAULT 'YJ' NOT NULL -- 기본값 'YJ'
);
