clear all;,close all; % すべてのグローバル変数/ウィンドを消去
% STEP(1)
X=load("sample2d.txt"); % sample2d.txt の読み込み

% STEP(2)
[d,n]=size(X); % X の次元d とサンプル数n を取得
R=zeros(d,1);
m=mean(X,2); % サンプルの平均値
for ii = 1 : n
	R=R+(X(:,ii)*X(:,ii)'); 
end
R=R./n;
cv=R-(m*m');

% STEP(3)
[v, lambda] = eig(cv); % 固有ベクトルと固有値を取得

% STEP(4)
[sorteigen, order] = sort(diag(lambda),'descend'); % 固有値をソートする
U = v(:,order); % 同じやり方で固有ベクトル内をソーティング
u=U(:,1); % 最大固有値に対する固有ベクトル

% STEP(5)
slope=u(2)/u(1); % 直線の傾き
xx=[min(X(1,:)):.05:max(X(1,:))];
figure(1),clf,hold on,plot(X(1,:),X(2,:),"bo"); % サンプルを2 次元平面に青点でプロット
figure(1),plot(xx,slope.*xx+m(2)-slope.*m(1),"g-"); % 直線0.1x+0.1 を緑の直線で描画
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