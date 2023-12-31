CREATE DATABASE QLSinhVien
go
use QLSinhVien
go

CREATE TABLE Lop(
	ID int IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	TenLop nvarchar(20) NOT NULL)

CREATE TABLE SinhVien(
	ID int IDENTITY(1, 1) NOT NULL PRIMARY KEY,
	HoTen nvarchar(100) NOT NULL,
	MaLop int NULL)

INSERT Lop (TenLop) VALUES (N'CTK43')
INSERT Lop (TenLop) VALUES (N'CTK44A')
INSERT Lop (TenLop) VALUES (N'CTK44B')
INSERT Lop (TenLop) VALUES (N'CTK45A')

INSERT SinhVien (HoTen, MaLop) VALUES (N'Trần Văn Thái wewr', 1)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Mai Thành Thân', 2)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Phạm Thanh Thảo', 2)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Trần Quốc Bảo Trung', 3)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Thái Thành Lam', 3)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Trần Văn Tám', 3)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Nguyễn Công Thành', 4)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Nguyễn Thị Lụa', 1)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Phan Thanh Nga', 1)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Trương Công Quyền', 4)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Võ Thị Sáu', 1)
INSERT SinhVien (HoTen, MaLop) VALUES (N'Võ Tòng', 2)

CREATE PROC InsertStudent
	@Id int,
	@HoTen nvarchar(100),
	@MaLop int
AS
BEGIN
	INSERT INTO SinhVien
	VALUES (@Id, @HoTen, @MaLop)
END

select * from Lop



