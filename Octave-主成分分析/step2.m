% STEP(1): �听�����͂�Zi�����߂�
clear all;,close all; % ���ׂẴO���[�o���ϐ�/�E�B���h������
X=load("iris4d.txt"); % iris4d.txt �̓ǂݍ���
[d,n]=size(X); % X �̎���d �ƃT���v����n ���擾
R=zeros(d,1);
m=mean(X,2); % �T���v���̕��ϒl
for ii = 1 : n
	R=R+(X(:,ii)*X(:,ii)'); 
end
R=R./n;
cv=R-(m*m');
[v, lambda] = eig(cv); % �ŗL�x�N�g���ƌŗL�l���擾
[sorteigen, order] = sort(diag(lambda),'descend'); % �ŗL�l���\�[�g����
U = v(:,order); % ���������ŌŗL�x�N�g�������\�[�e�B���O
u=U(:,1:2); % �ő�ŗL�l�ɑ΂���ŗL�x�N�g��2�{
Z=zeros(2,n);% Zi�����߂�
for i = 1 : n
	Z(:,i)=u'*(X(:,i)-m);
end
% STEP(2):���z�̏o��
% Zi��3��ނ̉Ԃɕ���
x1 = Z(1,1:50); % setosa
y1 = Z(2,1:50); 
x2 = Z(1,51:100); % versicolor
y2 = Z(2,51:100); 
x3 = Z(1,101:150); % virginica
y3 = Z(2,101:150); 
% 2�����ł̕��z���o�͂���
xx=[min(X(1,:)):.05:max(X(1,:))];
figure(1),clf,hold on,plot(x1,y1,"ro"); % setosa��Ԃ��ۂ�
figure(1),plot(x2,y2,"go"); % versicolor��΂̊ۂ�
figure(1),plot(x3,y3,"bo"); % virginica����ۂ�
% STEP(3):�ݐϊ�^�����v�Z���āA�O���t���쐬����
% ���ׂĂ̌ŗL�l�̑��a
lambda_d=0;
for i = 1 : d
	lambda_d=lambda_d+sorteigen(i);
end
% ���r �̌ŗL�l�i���U�j�̑��a
lambda_R=zeros(d,1);
lambda_R(1)=sorteigen(1);
for i = 2 : d
	lambda_R(i)=lambda_R(i-1)+sorteigen(i);
end
% �ݐϊ�^����ۑ�����x�N�g��
rate=zeros(d,1);
% r=1,2,3,4�̏ꍇ�̗ݐϊ�^����rate�Ɋi�[
for i = 1 : d
	rate(i)=lambda_R(i)/lambda_d;
end
% ��^�����O���t������
r=[1,2,3,4];
figure(2),hold on,plot(r,rate,"ro-");
axis square;