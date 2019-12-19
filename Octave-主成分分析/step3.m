% STEP(1):固有値を求め、降順に並べた後に、対応する固有ベクトルも並べ替える
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

% STEP(2): 誤差errorを求める
error=zeros(d,1);

for i = 1:d
	u=U(:,1:i); % 最大固有値に対する固有ベクトルi本
	Z=zeros(i,n); % Ziを求める 
	for j = 1 : n
		Z(:,j)=u'*(X(:,j)-m);
	end

	X_new=zeros(d,n); % 式（6）で~Xiを求める（X_new）
	for j = 1 : n
		X_new(:,j)=m+(u*Z(:,j));
	end

	for j = 1 : n % 誤さ平均値の計算
		error(i)=error(i)+((X(:,j)-X_new(:,j))'*(X(:,j)-X_new(:,j)));
	end
	error(i)=error(i)./n;
	
end
% STEP(3): 誤差のグラフを出力
% 次元数毎の誤差の平均値をkekkaに格納
kekka=[[1,2,3,4];error'];
figure(1),clf,hold on,plot(kekka(1,:),kekka(2,:),"bo");
