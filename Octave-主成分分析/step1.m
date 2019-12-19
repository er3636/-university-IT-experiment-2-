clear all;,close all; % ���ׂẴO���[�o���ϐ�/�E�B���h������
% STEP(1)
X=load("sample2d.txt"); % sample2d.txt �̓ǂݍ���

% STEP(2)
[d,n]=size(X); % X �̎���d �ƃT���v����n ���擾
R=zeros(d,1);
m=mean(X,2); % �T���v���̕��ϒl
for ii = 1 : n
	R=R+(X(:,ii)*X(:,ii)'); 
end
R=R./n;
cv=R-(m*m');

% STEP(3)
[v, lambda] = eig(cv); % �ŗL�x�N�g���ƌŗL�l���擾

% STEP(4)
[sorteigen, order] = sort(diag(lambda),'descend'); % �ŗL�l���\�[�g����
U = v(:,order); % ���������ŌŗL�x�N�g�������\�[�e�B���O
u=U(:,1); % �ő�ŗL�l�ɑ΂���ŗL�x�N�g��

% STEP(5)
slope=u(2)/u(1); % �����̌X��
xx=[min(X(1,:)):.05:max(X(1,:))];
figure(1),clf,hold on,plot(X(1,:),X(2,:),"bo"); % �T���v����2 �������ʂɐ_�Ńv���b�g
figure(1),plot(xx,slope.*xx+m(2)-slope.*m(1),"g-"); % ����0.1x+0.1 ��΂̒����ŕ`��
axis square;

% STEP(6)
Z=zeros(n,1);
for i = 1 : n
	Z(i)=X'(i,:)*u;
end

% STEP(6) -version2-
Z2=zeros(1,n);
for i = 1 : n
	Z2(i)=u'*(X(:,i)-m);
end
Z_bunsan=u'*cv*u;