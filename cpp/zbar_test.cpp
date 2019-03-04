#include <stdio.h>
#include <iostream>

#include "opencv2/highgui.hpp"
#include "opencv2/opencv.hpp"
#include "zbar.h"

using namespace cv;
using namespace zbar;
using namespace std;

int main(int argc, char ** argv)
{
	ImageScanner scanner;    
	scanner.set_config(ZBAR_NONE, ZBAR_CFG_ENABLE, 1);  

  Mat image = imread("/home/wxx/图片/th.jpeg");
  Mat imageGray;
  cvtColor(image,imageGray,CV_RGB2GRAY); 
	int width = imageGray.cols;    
	int height = imageGray.rows;    
  uchar *raw = (uchar *)imageGray.data;
  Image imageZbar(width, height, "Y800", raw, width * height);
	scanner.scan(imageZbar); //扫描条码  
  Image::SymbolIterator symbol = imageZbar.symbol_begin();
	if(symbol==imageZbar.symbol_end())
	{
		cout<<"查询条码失败，请检查图片！"<<endl;
	}
	for(;symbol != imageZbar.symbol_end();++symbol)  
	{    
		cout<<"类型："<<endl<<symbol->get_type_name()<<endl<<endl;  
		cout<<"条码："<<endl<<symbol->get_data()<<endl<<endl;
		//获取二维码坐标
		/*	get_location  index0-3
				0--3
				|  |
				1--2
		*/
		int x0 = symbol->get_location_x(0);
		int y0 = symbol->get_location_y(0);
		int x1 = symbol->get_location_x(1);
		int y1 = symbol->get_location_y(1);
		int x2 = symbol->get_location_x(2);
		int y2 = symbol->get_location_y(2);
		int x3 = symbol->get_location_x(3);
		int y3 = symbol->get_location_y(3);
		int size = symbol->get_location_size();
		cout<<"("<<x0<<" , "<<y0<<")"<<endl;
		cout<<"("<<x1<<" , "<<y1<<")"<<endl;
		cout<<"("<<x2<<" , "<<y2<<")"<<endl;
		cout<<"("<<x3<<" , "<<y3<<")"<<endl;
		circle(image, Point(x0, y0),5, Scalar(0,0,255), 3);
		circle(image, Point(x1, y1),5, Scalar(255,0,0), 3);
		circle(image, Point(x2, y2),5, Scalar(0,255,0), 3);
	}    
	imshow("Source Image",image); 
	imshow("imageGray",imageGray);       
	waitKey(-1);
  imageZbar.set_data(NULL,0);
  printf("hello world qrcode_detector package\n");
  return 0;
}