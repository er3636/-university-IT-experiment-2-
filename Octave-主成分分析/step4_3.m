clear all;,close all; % ���ׂẴO���[�o���ϐ�/�E�B���h������
X=load("SomervilleHappinessSurvey2015.txt"); % data5d.xls �̓ǂݍ���
X=X';
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
Z=zeros(2,n);
for i = 1 : n
	Z(:,i)=u'*(X(:,i)-m);
end
x1 = Z(1,1:66); % setosa
y1 = Z(2,1:66); 
x2 = Z(1,67:143); % versicolor
y2 = Z(2,67:143); 

xx=[min(X(1,:)):.05:max(X(1,:))];
figure(1),clf,hold on,plot(x1,y1,"ro"); % setosa��Ԃ��ۂ�
figure(1),plot(x2,y2,"go"); % versicolor��΂̊ۂ�
%figure(2),plot(xx,slope.*xx+m(2)-slope.*m(1),'g-'); % ����0.1x+0.1 ��΂̒����ŕ`��
axis square;