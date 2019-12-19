clear all;,close all; % すべてのグローバル変数/ウィンドを消去
X=load("SomervilleHappinessSurvey2015.txt"); % data5d.xls の読み込み
X=X';
[d,n]=size(X); % X の次元d とサンプル数n を取得
R=zeros(d,1);
m=mean(X,2); % サンプルの平均値
for ii = 1 : n
	R=R+(X(:,ii)*X(:,ii)'); 
end
R=R./n;
cv=R-(m*m');
[v, lambda] = eig(cv); % 固有ベクトルと固有値を取得
[sorteigen, order] = sort(diag(lambda),'descend'); % 固有値をソートする
U = v(:,order); % 同じやり方で固有ベクトル内をソーティング
u=U(:,1:2); % 最大固有値に対する固有ベクトル2本
Z=zeros(2,n);
for i = 1 : n
	Z(:,i)=u'*(X(:,i)-m);
end
x1 = Z(1,1:66); % setosa
y1 = Z(2,1:66); 
x2 = Z(1,67:143); % versicolor
y2 = Z(2,67:143); 

xx=[min(X(1,:)):.05:max(X(1,:))];
figure(1),clf,hold on,plot(x1,y1,"ro"); % setosaを赤い丸で
figure(1),plot(x2,y2,"go"); % versicolorを緑の丸で
%figure(2),plot(xx,slope.*xx+m(2)-slope.*m(1),'g-'); % 直線0.1x+0.1 を緑の直線で描画
axis square;