-- MS-SQL
CREATE TABLE tbCafeList (
    idx INT PRIMARY KEY IDENTITY(1,1), -- auto increment 대체
    francise_name VARCHAR(MAX) NOT NULL, -- 한글 데이터를 고려하여 NVARCHAR 사용
    francise_addr VARCHAR(MAX) NOT NULL,
    francise_tel VARCHAR(MAX) NOT NULL,
    cafe_gubun INT NOT NULL CHECK (cafe_gubun IN (1, 2, 3)), -- CHECK 제약 조건 수정
    regTime DATETIME DEFAULT GETDATE() NOT NULL, -- 현재 시간을 기본값으로 설정
    regID VARCHAR(MAX) DEFAULT 'YJ' NOT NULL -- 기본값 설정
);




/* --MySQL
CREATE TABLE tbCafeList (
    idx INT AUTO_INCREMENT PRIMARY KEY, -- 자동 증가
    francise_name VARCHAR(255) NOT NULL, -- 최대 길이를 명시적으로 지정
    francise_addr VARCHAR(255) NOT NULL,
    francise_tel VARCHAR(255) NOT NULL,
    cafe_gubun INT NOT NULL CHECK (cafe_gubun IN (1, 2, 3)), -- CHECK 제약 조건
    regTime DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL, -- 기본값으로 현재 시간
    regID VARCHAR(255) DEFAULT 'YJ' NOT NULL -- 기본값 'YJ'
);
*/
