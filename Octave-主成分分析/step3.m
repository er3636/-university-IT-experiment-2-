% STEP(1):�ŗL�l�����߁A�~���ɕ��ׂ���ɁA�Ή�����ŗL�x�N�g�������בւ���
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

% STEP(2): �덷error�����߂�
error=zeros(d,1);

for i = 1:d
	u=U(:,1:i); % �ő�ŗL�l�ɑ΂���ŗL�x�N�g��i�{
	Z=zeros(i,n); % Zi�����߂� 
	for j = 1 : n
		Z(:,j)=u'*(X(:,j)-m);
	end

	X_new=zeros(d,n); % ���i6�j��~Xi�����߂�iX_new�j
	for j = 1 : n
		X_new(:,j)=m+(u*Z(:,j));
	end

	for j = 1 : n % �낳���ϒl�̌v�Z
		error(i)=error(i)+((X(:,j)-X_new(:,j))'*(X(:,j)-X_new(:,j)));
	end
	error(i)=error(i)./n;
	
end
% STEP(3): �덷�̃O���t���o��
% ���������̌덷�̕��ϒl��kekka�Ɋi�[
kekka=[[1,2,3,4];error'];
figure(1),clf,hold on,plot(kekka(1,:),kekka(2,:),"bo");
