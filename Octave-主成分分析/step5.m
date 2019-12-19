clear all;,close all;

d=64;
n=16;

load olivettifaces; % https://cs.nyu.edu/~roweis/data.html からダウンロードした顔のデータセット
for i=1:n
	X(:,i)=faces(:,n.*(i-1)+1); % 16人の顔の画像データ（画像の画素値を縦に並べたベクトルからなる行列）
	a=reshape(X(:,i),[d d]); % 元の画像を png として出力するためにサイズ変換を行う
	a=uint8(a); % double型からint型へ変換
	namae=[num2str(i),".png"]; % 元の画像を保存するファイル名を指定
	imwrite(a,namae); % 画像の保存
end
m=mean(X,2); % サンプルの平均値
cv=cov(X'); % 共分散行列の計算
[v, lambda] = eig(cv); % 固有ベクトルと固有値を取得
[sorteigen, order] = sort(diag(lambda),'descend'); % 固有値をソートする
U = v(:,order); % 同じやり方で固有ベクトル内をソーティング
u=U(:,1:16); % 最大固有値に対する固有ベクトル

mean=reshape(m(:,1),[d d]);
mean=mean./255;
imshow(mean); % 平均ベクトル

% 新しい画像の出力・保存
for i = 1:n
  u(:,i)=u(:,i)-min(u(:,i));
  u(:,i)=u(:,i)./max(u(:,i));
	a=reshape(u(:,i),[d d]);
	namae=[num2str(i),"_new.png"]; %結果の保存
	figure(i);
  imshow(a);
  %imwrite(a.*256,namae);
  
end