# ���������� ��������
import array
# ������� (�������) ��� ����� �
Alp = {'�': 1, '�': 2, '�': 3, '�': 4, '�': 5, '�': 6, '�': 7, '�': 8, '�': 9, '�': 10, '�': 11, '�': 12, '�': 13, '�': 14, '�': 15, '�': 16, '�': 17, '�': 18, '�': 19, '�': 20, '�': 21, '�':22, '�':23, '�':24, '�':25, '�':26, '�':27, '�':28, '�':29, '�':30, '�':31, '�':32} #1-32
Dic = ['�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�', '�'] #1-32

# ��������-�������� ��������������� �1
# ����: ��������� �������� �����
# �����: �������� ������������������
def SymToCode(message):
	xarray = []
	length = len(message)
	ctr = 0
	while not ctr == length:
		xarray.append(Alp[message[ctr]])
		ctr = ctr +1
	return xarray

# �����-��������� ��������������� �2
# ����: �������� ������������������
# �����: ��������� �������� �����
def CodeToSym(imessage):
	Sym = ''
	length = len(imessage)
	itterator = 0
	while not itterator == length:
		Sym = Sym + Dic[imessage[itterator] - 1]
		itterator = itterator + 1
	return Sym

# �������� �������� �3
# ����: ���� �������� �������������������
# �����: ����� �������� ������������������� � ���������� ������ ����� ��������
def summator(message, key):
	lengthM = len(message)
	lengthK = len(key)
	itteratorM = 0
	itteratorK = 0	
	while not itteratorM == lengthM:
		if (itteratorK == lengthK):
			itteratorK = 0; 
		message[itteratorM] = message[itteratorM] + key[itteratorK]
                message[itteratotM] = message[itteratotM] % 32
		if(message[itteratorM] == 0):
			message[itteratorM] = 32
		itteratorM = itteratorM + 1
		itteratorK = itteratorK + 1
	return message

# �������� ����������
# ����: ���������1, ���������2, �������� �� ��������� 2 ������
# �����: ������� ���������
def deciminator(message1, message2, bkey):
	lengthM1 = len(message1)
	lengthM2 = len(message2)
	# ��������� ������ ���������
	# ��������� ��������� � ������ � ����� ����� �����������
	# ������� �������� ��������������� ��������� � ������ �������
	if (bkey == False):
		if(lengthM1 < lengthM2):
			buf = lengthM1
			lengthM1 = lenguhM2
			lengthM2 = 0
		else:
			lengthM2 = 0
	itteratorM1 = 0
	itteratorM2 = 0
	#while not itterator
	return 0

print('-> ��������� �������� � ������')
#cmd = input('-> dEscription or enCryption or keY: ')
#if (cmd == 'c'):
mesg = input('-> ������� ���������: ')
imesg = SymToCode(mesg)
imesg = imesg.upper()
print('-> �������� ��� ���������: ', imesg)
key = input('-> ������� ����: ')
ikey = SymToCode(key)
print('-> �������� ��� �����: ', ikey)
ires = summator(imesg, ikey)
res = CodeToSym(ires)
print('-> ��������� ����������: ', res)
print('-> �������� ��������� ��������� ����������: ', ires)
input('-> �����!')
#elif (cmd == 'e'):
#    print('hi')
#elif (cmd == 'y'):
#    print('hi')
#else: print('-> �������� �������')
