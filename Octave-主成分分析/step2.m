% STEP(1): 主成分分析でZiを求める
clear all;,close all; % すべてのグローバル変数/ウィンドを消去
X=load("iris4d.txt"); % iris4d.txt の読み込み
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
Z=zeros(2,n);% Ziを求める
for i = 1 : n
	Z(:,i)=u'*(X(:,i)-m);
end
% STEP(2):分布の出力
% Ziを3種類の花に分割
x1 = Z(1,1:50); % setosa
y1 = Z(2,1:50); 
x2 = Z(1,51:100); % versicolor
y2 = Z(2,51:100); 
x3 = Z(1,101:150); % virginica
y3 = Z(2,101:150); 
% 2次元での分布を出力する
xx=[min(X(1,:)):.05:max(X(1,:))];
figure(1),clf,hold on,plot(x1,y1,"ro"); % setosaを赤い丸で
figure(1),plot(x2,y2,"go"); % versicolorを緑の丸で
figure(1),plot(x3,y3,"bo"); % virginicaを青い丸で
% STEP(3):累積寄与率を計算して、グラフを作成する
% すべての固有値の総和
lambda_d=0;
for i = 1 : d
	lambda_d=lambda_d+sorteigen(i);
end
% 上位r 個の固有値（分散）の総和
lambda_R=zeros(d,1);
lambda_R(1)=sorteigen(1);
for i = 2 : d
	lambda_R(i)=lambda_R(i-1)+sorteigen(i);
end
% 累積寄与率を保存するベクトル
rate=zeros(d,1);
% r=1,2,3,4の場合の累積寄与率をrateに格納
for i = 1 : d
	rate(i)=lambda_R(i)/lambda_d;
end
% 寄与率をグラフ化する
r=[1,2,3,4];
figure(2),hold on,plot(r,rate,"ro-");
axis square;