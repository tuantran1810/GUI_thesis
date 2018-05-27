/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.11.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDoubleSpinBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGraphicsView>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QFrame *Plate_Controller_Fr;
    QLabel *Plate_Controller_La;
    QPushButton *Plate_Controller_Apply_Bu;
    QGroupBox *Plate_Controller_PID_GB;
    QDoubleSpinBox *PID_Kd_Box;
    QLabel *PID_Kp_La;
    QLabel *PID_Kd_La;
    QDoubleSpinBox *PID_Ki_Box;
    QDoubleSpinBox *PID_Kp_Box;
    QLabel *PID_Ki_La;
    QGroupBox *Plate_Controller_SMC_GB;
    QDoubleSpinBox *SMC_k1_Box;
    QDoubleSpinBox *SMC_K_Box;
    QLabel *SMC_k1_La;
    QLabel *SMC_K_La;
    QRadioButton *Plate_Controller_PID_Ch;
    QRadioButton *Plate_Controller_SMC_Ch;
    QFrame *Mode_Fr;
    QLabel *Mode_La;
    QGroupBox *Mode_Circle_GB;
    QLabel *Circle_R_La;
    QLabel *Circle_CentralY_La;
    QLabel *Circle_CentralX_La;
    QSpinBox *Circle_R_Box;
    QSpinBox *Circle_CentralX_Box;
    QSpinBox *Circle_CentralY_Box;
    QGroupBox *Mode_Rectangle_RB;
    QLabel *Rectangle_TopLeftX_La;
    QLabel *Rectangle_BotRightX_La;
    QLabel *Rectangle_TopLeftY_La;
    QLabel *Rectangle_BotRightY_La;
    QSpinBox *Rectangle_TopLeftX_Box;
    QSpinBox *Rectangle_TopLeftY_Box;
    QSpinBox *Rectangle_BotRightX_Box;
    QSpinBox *Rectangle_BotRightY_Box;
    QGroupBox *Mode_FreeSet_GB;
    QLabel *FreeSet_X_La;
    QLabel *FreeSet_Y_La;
    QSpinBox *FreeSet_X_Box;
    QSpinBox *FreeSet_Y_Box;
    QPushButton *Mode_Apply_Bu;
    QRadioButton *Mode_Circle_Ch;
    QRadioButton *Mode_Rectangle_Ch;
    QRadioButton *Mode_FreeSet_Ch;
    QGraphicsView *PlateView_Gra;
    QGraphicsView *XAxist_Angle_Gra;
    QGraphicsView *YAxist_Angle_Gra;
    QLabel *PlateView_La;
    QLabel *XAxist_Angle_La;
    QLabel *YAxist_Angle_La;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(660, 628);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        Plate_Controller_Fr = new QFrame(centralWidget);
        Plate_Controller_Fr->setObjectName(QStringLiteral("Plate_Controller_Fr"));
        Plate_Controller_Fr->setGeometry(QRect(10, 10, 311, 211));
        Plate_Controller_Fr->setFrameShape(QFrame::StyledPanel);
        Plate_Controller_Fr->setFrameShadow(QFrame::Raised);
        Plate_Controller_La = new QLabel(Plate_Controller_Fr);
        Plate_Controller_La->setObjectName(QStringLiteral("Plate_Controller_La"));
        Plate_Controller_La->setGeometry(QRect(10, 0, 101, 21));
        Plate_Controller_Apply_Bu = new QPushButton(Plate_Controller_Fr);
        Plate_Controller_Apply_Bu->setObjectName(QStringLiteral("Plate_Controller_Apply_Bu"));
        Plate_Controller_Apply_Bu->setGeometry(QRect(22, 170, 271, 32));
        Plate_Controller_PID_GB = new QGroupBox(Plate_Controller_Fr);
        Plate_Controller_PID_GB->setObjectName(QStringLiteral("Plate_Controller_PID_GB"));
        Plate_Controller_PID_GB->setGeometry(QRect(20, 40, 121, 131));
        PID_Kd_Box = new QDoubleSpinBox(Plate_Controller_PID_GB);
        PID_Kd_Box->setObjectName(QStringLiteral("PID_Kd_Box"));
        PID_Kd_Box->setGeometry(QRect(30, 90, 81, 24));
        PID_Kd_Box->setDecimals(4);
        PID_Kd_Box->setMinimum(-999.99);
        PID_Kd_Box->setMaximum(999.99);
        PID_Kd_Box->setSingleStep(0.1);
        PID_Kp_La = new QLabel(Plate_Controller_PID_GB);
        PID_Kp_La->setObjectName(QStringLiteral("PID_Kp_La"));
        PID_Kp_La->setGeometry(QRect(10, 30, 21, 16));
        PID_Kp_La->setLineWidth(2);
        PID_Kd_La = new QLabel(Plate_Controller_PID_GB);
        PID_Kd_La->setObjectName(QStringLiteral("PID_Kd_La"));
        PID_Kd_La->setGeometry(QRect(10, 90, 21, 16));
        PID_Kd_La->setLineWidth(2);
        PID_Ki_Box = new QDoubleSpinBox(Plate_Controller_PID_GB);
        PID_Ki_Box->setObjectName(QStringLiteral("PID_Ki_Box"));
        PID_Ki_Box->setGeometry(QRect(30, 60, 81, 24));
        PID_Ki_Box->setDecimals(4);
        PID_Ki_Box->setMinimum(-999.99);
        PID_Ki_Box->setMaximum(999.99);
        PID_Ki_Box->setSingleStep(0.1);
        PID_Kp_Box = new QDoubleSpinBox(Plate_Controller_PID_GB);
        PID_Kp_Box->setObjectName(QStringLiteral("PID_Kp_Box"));
        PID_Kp_Box->setGeometry(QRect(30, 30, 81, 24));
        PID_Kp_Box->setDecimals(4);
        PID_Kp_Box->setMinimum(-999.99);
        PID_Kp_Box->setMaximum(999.99);
        PID_Kp_Box->setSingleStep(0.1);
        PID_Ki_La = new QLabel(Plate_Controller_PID_GB);
        PID_Ki_La->setObjectName(QStringLiteral("PID_Ki_La"));
        PID_Ki_La->setGeometry(QRect(10, 60, 21, 16));
        PID_Ki_La->setLineWidth(2);
        Plate_Controller_SMC_GB = new QGroupBox(Plate_Controller_Fr);
        Plate_Controller_SMC_GB->setObjectName(QStringLiteral("Plate_Controller_SMC_GB"));
        Plate_Controller_SMC_GB->setGeometry(QRect(170, 40, 121, 101));
        SMC_k1_Box = new QDoubleSpinBox(Plate_Controller_SMC_GB);
        SMC_k1_Box->setObjectName(QStringLiteral("SMC_k1_Box"));
        SMC_k1_Box->setGeometry(QRect(30, 60, 81, 24));
        SMC_k1_Box->setDecimals(4);
        SMC_k1_Box->setMinimum(-999.99);
        SMC_k1_Box->setMaximum(999.99);
        SMC_k1_Box->setSingleStep(0.1);
        SMC_K_Box = new QDoubleSpinBox(Plate_Controller_SMC_GB);
        SMC_K_Box->setObjectName(QStringLiteral("SMC_K_Box"));
        SMC_K_Box->setGeometry(QRect(30, 30, 81, 24));
        SMC_K_Box->setDecimals(4);
        SMC_K_Box->setMinimum(-999.99);
        SMC_K_Box->setMaximum(999.99);
        SMC_K_Box->setSingleStep(0.1);
        SMC_k1_La = new QLabel(Plate_Controller_SMC_GB);
        SMC_k1_La->setObjectName(QStringLiteral("SMC_k1_La"));
        SMC_k1_La->setGeometry(QRect(10, 60, 21, 16));
        SMC_k1_La->setLineWidth(2);
        SMC_K_La = new QLabel(Plate_Controller_SMC_GB);
        SMC_K_La->setObjectName(QStringLiteral("SMC_K_La"));
        SMC_K_La->setGeometry(QRect(10, 30, 21, 16));
        SMC_K_La->setLineWidth(2);
        Plate_Controller_PID_Ch = new QRadioButton(Plate_Controller_Fr);
        Plate_Controller_PID_Ch->setObjectName(QStringLiteral("Plate_Controller_PID_Ch"));
        Plate_Controller_PID_Ch->setGeometry(QRect(20, 20, 51, 20));
        Plate_Controller_SMC_Ch = new QRadioButton(Plate_Controller_Fr);
        Plate_Controller_SMC_Ch->setObjectName(QStringLiteral("Plate_Controller_SMC_Ch"));
        Plate_Controller_SMC_Ch->setGeometry(QRect(170, 20, 51, 20));
        Mode_Fr = new QFrame(centralWidget);
        Mode_Fr->setObjectName(QStringLiteral("Mode_Fr"));
        Mode_Fr->setGeometry(QRect(9, 240, 311, 381));
        Mode_Fr->setFrameShape(QFrame::StyledPanel);
        Mode_Fr->setFrameShadow(QFrame::Raised);
        Mode_La = new QLabel(Mode_Fr);
        Mode_La->setObjectName(QStringLiteral("Mode_La"));
        Mode_La->setGeometry(QRect(10, 0, 101, 21));
        Mode_Circle_GB = new QGroupBox(Mode_Fr);
        Mode_Circle_GB->setObjectName(QStringLiteral("Mode_Circle_GB"));
        Mode_Circle_GB->setGeometry(QRect(10, 40, 291, 91));
        Circle_R_La = new QLabel(Mode_Circle_GB);
        Circle_R_La->setObjectName(QStringLiteral("Circle_R_La"));
        Circle_R_La->setGeometry(QRect(10, 30, 21, 16));
        Circle_R_La->setLineWidth(2);
        Circle_CentralY_La = new QLabel(Mode_Circle_GB);
        Circle_CentralY_La->setObjectName(QStringLiteral("Circle_CentralY_La"));
        Circle_CentralY_La->setGeometry(QRect(190, 30, 61, 16));
        Circle_CentralY_La->setLineWidth(2);
        Circle_CentralX_La = new QLabel(Mode_Circle_GB);
        Circle_CentralX_La->setObjectName(QStringLiteral("Circle_CentralX_La"));
        Circle_CentralX_La->setGeometry(QRect(100, 30, 61, 16));
        Circle_CentralX_La->setLineWidth(2);
        Circle_R_Box = new QSpinBox(Mode_Circle_GB);
        Circle_R_Box->setObjectName(QStringLiteral("Circle_R_Box"));
        Circle_R_Box->setGeometry(QRect(10, 50, 81, 24));
        Circle_R_Box->setMaximum(120);
        Circle_CentralX_Box = new QSpinBox(Mode_Circle_GB);
        Circle_CentralX_Box->setObjectName(QStringLiteral("Circle_CentralX_Box"));
        Circle_CentralX_Box->setGeometry(QRect(100, 50, 81, 24));
        Circle_CentralX_Box->setMaximum(320);
        Circle_CentralY_Box = new QSpinBox(Mode_Circle_GB);
        Circle_CentralY_Box->setObjectName(QStringLiteral("Circle_CentralY_Box"));
        Circle_CentralY_Box->setGeometry(QRect(190, 50, 81, 24));
        Circle_CentralY_Box->setMaximum(320);
        Mode_Rectangle_RB = new QGroupBox(Mode_Fr);
        Mode_Rectangle_RB->setObjectName(QStringLiteral("Mode_Rectangle_RB"));
        Mode_Rectangle_RB->setGeometry(QRect(10, 130, 291, 141));
        Rectangle_TopLeftX_La = new QLabel(Mode_Rectangle_RB);
        Rectangle_TopLeftX_La->setObjectName(QStringLiteral("Rectangle_TopLeftX_La"));
        Rectangle_TopLeftX_La->setGeometry(QRect(40, 30, 81, 16));
        Rectangle_TopLeftX_La->setLineWidth(2);
        Rectangle_BotRightX_La = new QLabel(Mode_Rectangle_RB);
        Rectangle_BotRightX_La->setObjectName(QStringLiteral("Rectangle_BotRightX_La"));
        Rectangle_BotRightX_La->setGeometry(QRect(170, 30, 101, 16));
        Rectangle_BotRightX_La->setLineWidth(2);
        Rectangle_TopLeftY_La = new QLabel(Mode_Rectangle_RB);
        Rectangle_TopLeftY_La->setObjectName(QStringLiteral("Rectangle_TopLeftY_La"));
        Rectangle_TopLeftY_La->setGeometry(QRect(40, 80, 71, 16));
        Rectangle_TopLeftY_La->setLineWidth(2);
        Rectangle_BotRightY_La = new QLabel(Mode_Rectangle_RB);
        Rectangle_BotRightY_La->setObjectName(QStringLiteral("Rectangle_BotRightY_La"));
        Rectangle_BotRightY_La->setGeometry(QRect(170, 80, 101, 16));
        Rectangle_BotRightY_La->setLineWidth(2);
        Rectangle_TopLeftX_Box = new QSpinBox(Mode_Rectangle_RB);
        Rectangle_TopLeftX_Box->setObjectName(QStringLiteral("Rectangle_TopLeftX_Box"));
        Rectangle_TopLeftX_Box->setGeometry(QRect(40, 50, 81, 24));
        Rectangle_TopLeftX_Box->setMaximum(320);
        Rectangle_TopLeftY_Box = new QSpinBox(Mode_Rectangle_RB);
        Rectangle_TopLeftY_Box->setObjectName(QStringLiteral("Rectangle_TopLeftY_Box"));
        Rectangle_TopLeftY_Box->setGeometry(QRect(40, 100, 81, 24));
        Rectangle_TopLeftY_Box->setMaximum(320);
        Rectangle_BotRightX_Box = new QSpinBox(Mode_Rectangle_RB);
        Rectangle_BotRightX_Box->setObjectName(QStringLiteral("Rectangle_BotRightX_Box"));
        Rectangle_BotRightX_Box->setGeometry(QRect(170, 50, 81, 24));
        Rectangle_BotRightX_Box->setMaximum(320);
        Rectangle_BotRightY_Box = new QSpinBox(Mode_Rectangle_RB);
        Rectangle_BotRightY_Box->setObjectName(QStringLiteral("Rectangle_BotRightY_Box"));
        Rectangle_BotRightY_Box->setGeometry(QRect(170, 100, 81, 24));
        Rectangle_BotRightY_Box->setMaximum(320);
        Mode_FreeSet_GB = new QGroupBox(Mode_Fr);
        Mode_FreeSet_GB->setObjectName(QStringLiteral("Mode_FreeSet_GB"));
        Mode_FreeSet_GB->setGeometry(QRect(10, 270, 291, 71));
        FreeSet_X_La = new QLabel(Mode_FreeSet_GB);
        FreeSet_X_La->setObjectName(QStringLiteral("FreeSet_X_La"));
        FreeSet_X_La->setGeometry(QRect(20, 30, 21, 16));
        FreeSet_X_La->setLineWidth(2);
        FreeSet_Y_La = new QLabel(Mode_FreeSet_GB);
        FreeSet_Y_La->setObjectName(QStringLiteral("FreeSet_Y_La"));
        FreeSet_Y_La->setGeometry(QRect(150, 30, 16, 16));
        FreeSet_Y_La->setLineWidth(2);
        FreeSet_X_Box = new QSpinBox(Mode_FreeSet_GB);
        FreeSet_X_Box->setObjectName(QStringLiteral("FreeSet_X_Box"));
        FreeSet_X_Box->setGeometry(QRect(40, 30, 81, 24));
        FreeSet_X_Box->setMaximum(320);
        FreeSet_Y_Box = new QSpinBox(Mode_FreeSet_GB);
        FreeSet_Y_Box->setObjectName(QStringLiteral("FreeSet_Y_Box"));
        FreeSet_Y_Box->setGeometry(QRect(170, 30, 81, 24));
        FreeSet_Y_Box->setMaximum(320);
        Mode_Apply_Bu = new QPushButton(Mode_Fr);
        Mode_Apply_Bu->setObjectName(QStringLiteral("Mode_Apply_Bu"));
        Mode_Apply_Bu->setGeometry(QRect(12, 340, 291, 32));
        Mode_Circle_Ch = new QRadioButton(Mode_Fr);
        Mode_Circle_Ch->setObjectName(QStringLiteral("Mode_Circle_Ch"));
        Mode_Circle_Ch->setGeometry(QRect(10, 20, 61, 20));
        Mode_Rectangle_Ch = new QRadioButton(Mode_Fr);
        Mode_Rectangle_Ch->setObjectName(QStringLiteral("Mode_Rectangle_Ch"));
        Mode_Rectangle_Ch->setGeometry(QRect(100, 20, 91, 20));
        Mode_FreeSet_Ch = new QRadioButton(Mode_Fr);
        Mode_FreeSet_Ch->setObjectName(QStringLiteral("Mode_FreeSet_Ch"));
        Mode_FreeSet_Ch->setGeometry(QRect(210, 20, 81, 20));
        PlateView_Gra = new QGraphicsView(centralWidget);
        PlateView_Gra->setObjectName(QStringLiteral("PlateView_Gra"));
        PlateView_Gra->setGeometry(QRect(330, 20, 320, 320));
        PlateView_Gra->setInteractive(true);
        XAxist_Angle_Gra = new QGraphicsView(centralWidget);
        XAxist_Angle_Gra->setObjectName(QStringLiteral("XAxist_Angle_Gra"));
        XAxist_Angle_Gra->setGeometry(QRect(330, 360, 320, 120));
        YAxist_Angle_Gra = new QGraphicsView(centralWidget);
        YAxist_Angle_Gra->setObjectName(QStringLiteral("YAxist_Angle_Gra"));
        YAxist_Angle_Gra->setGeometry(QRect(330, 500, 320, 120));
        PlateView_La = new QLabel(centralWidget);
        PlateView_La->setObjectName(QStringLiteral("PlateView_La"));
        PlateView_La->setGeometry(QRect(330, 0, 91, 16));
        XAxist_Angle_La = new QLabel(centralWidget);
        XAxist_Angle_La->setObjectName(QStringLiteral("XAxist_Angle_La"));
        XAxist_Angle_La->setGeometry(QRect(330, 340, 91, 16));
        YAxist_Angle_La = new QLabel(centralWidget);
        YAxist_Angle_La->setObjectName(QStringLiteral("YAxist_Angle_La"));
        YAxist_Angle_La->setGeometry(QRect(330, 480, 91, 16));
        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Ball And Plate Control Panel", nullptr));
        Plate_Controller_La->setText(QApplication::translate("MainWindow", "Plate Controller", nullptr));
        Plate_Controller_Apply_Bu->setText(QApplication::translate("MainWindow", "Apply", nullptr));
        Plate_Controller_PID_GB->setTitle(QApplication::translate("MainWindow", "PID Controller", nullptr));
        PID_Kp_La->setText(QApplication::translate("MainWindow", "Kp", nullptr));
        PID_Kd_La->setText(QApplication::translate("MainWindow", "Kd", nullptr));
        PID_Ki_La->setText(QApplication::translate("MainWindow", "Ki", nullptr));
        Plate_Controller_SMC_GB->setTitle(QApplication::translate("MainWindow", "Sliding Mode Control", nullptr));
        SMC_k1_La->setText(QApplication::translate("MainWindow", "k1", nullptr));
        SMC_K_La->setText(QApplication::translate("MainWindow", "K", nullptr));
        Plate_Controller_PID_Ch->setText(QApplication::translate("MainWindow", "PID", nullptr));
        Plate_Controller_SMC_Ch->setText(QApplication::translate("MainWindow", "SMC", nullptr));
        Mode_La->setText(QApplication::translate("MainWindow", "Mode", nullptr));
        Mode_Circle_GB->setTitle(QApplication::translate("MainWindow", "Circle Mode", nullptr));
        Circle_R_La->setText(QApplication::translate("MainWindow", "R", nullptr));
        Circle_CentralY_La->setText(QApplication::translate("MainWindow", "Central Y", nullptr));
        Circle_CentralX_La->setText(QApplication::translate("MainWindow", "Central X", nullptr));
        Mode_Rectangle_RB->setTitle(QApplication::translate("MainWindow", "Rectangle Mode", nullptr));
        Rectangle_TopLeftX_La->setText(QApplication::translate("MainWindow", "Top Left X", nullptr));
        Rectangle_BotRightX_La->setText(QApplication::translate("MainWindow", "Bottom Right X", nullptr));
        Rectangle_TopLeftY_La->setText(QApplication::translate("MainWindow", "Top Left Y", nullptr));
        Rectangle_BotRightY_La->setText(QApplication::translate("MainWindow", "Bottom Right Y", nullptr));
        Mode_FreeSet_GB->setTitle(QApplication::translate("MainWindow", "Free Set Mode", nullptr));
        FreeSet_X_La->setText(QApplication::translate("MainWindow", "X", nullptr));
        FreeSet_Y_La->setText(QApplication::translate("MainWindow", "Y", nullptr));
        Mode_Apply_Bu->setText(QApplication::translate("MainWindow", "Apply", nullptr));
        Mode_Circle_Ch->setText(QApplication::translate("MainWindow", "Circle", nullptr));
        Mode_Rectangle_Ch->setText(QApplication::translate("MainWindow", "Rectangle", nullptr));
        Mode_FreeSet_Ch->setText(QApplication::translate("MainWindow", "Free Set", nullptr));
        PlateView_La->setText(QApplication::translate("MainWindow", "Plate View", nullptr));
        XAxist_Angle_La->setText(QApplication::translate("MainWindow", "X Axist Angle", nullptr));
        YAxist_Angle_La->setText(QApplication::translate("MainWindow", "Y Axist Angle", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
