clear all;,close all;

d=64;
n=16;

load olivettifaces; % https://cs.nyu.edu/~roweis/data.html ����_�E�����[�h������̃f�[�^�Z�b�g
for i=1:n
	X(:,i)=faces(:,n.*(i-1)+1); % 16�l�̊�̉摜�f�[�^�i�摜�̉�f�l���c�ɕ��ׂ��x�N�g������Ȃ�s��j
	a=reshape(X(:,i),[d d]); % ���̉摜�� png �Ƃ��ďo�͂��邽�߂ɃT�C�Y�ϊ����s��
	a=uint8(a); % double�^����int�^�֕ϊ�
	namae=[num2str(i),".png"]; % ���̉摜��ۑ�����t�@�C�������w��
	imwrite(a,namae); % �摜�̕ۑ�
end
m=mean(X,2); % �T���v���̕��ϒl
cv=cov(X'); % �����U�s��̌v�Z
[v, lambda] = eig(cv); % �ŗL�x�N�g���ƌŗL�l���擾
[sorteigen, order] = sort(diag(lambda),'descend'); % �ŗL�l���\�[�g����
U = v(:,order); % ���������ŌŗL�x�N�g�������\�[�e�B���O
u=U(:,1:16); % �ő�ŗL�l�ɑ΂���ŗL�x�N�g��

mean=reshape(m(:,1),[d d]);
mean=mean./255;
imshow(mean); % ���σx�N�g��

% �V�����摜�̏o�́E�ۑ�
for i = 1:n
  u(:,i)=u(:,i)-min(u(:,i));
  u(:,i)=u(:,i)./max(u(:,i));
	a=reshape(u(:,i),[d d]);
	namae=[num2str(i),"_new.png"]; %���ʂ̕ۑ�
	figure(i);
  imshow(a);
  %imwrite(a.*256,namae);
  
end