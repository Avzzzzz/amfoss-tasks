import 'package:codiing_demo/models/onboarding_info.dart';
import 'package:flutter/material.dart';
import 'package:get/state_manager.dart';
import 'package:get/utils.dart';
class OnboardingController extends GetxController 
{
  var selectedPageIndex = 0.obs;
  bool get isLastPage => selectedPageIndex.value == onboardingPages.length - 1;
  var pageController = PageController();
  forwardAction()
  { if (isLastPage)  {
    
    //go to home page
  }
     
     pageController.nextPage(duration: 300.milliseconds, curve: Curves.ease);


  }
  List<OnboardingInfo> onboardingPages = [
    OnboardingInfo('assets/page1.png', 'YOGA SURGE', 'Inhale the future,exhale the past'),
    OnboardingInfo('assets/page2.png', 'Healthy Freaks Excercises', 'Letting go is the hardest asana'),
    OnboardingInfo('assets/page3.png', 'Cycling', 'You cannot always control what goes on outside.But you can always control what goes on inside '),
    OnboardingInfo('assets/page4.png', 'Meditation', 'The longest journey of any person is the journey inward.'),
    OnboardingInfo('assets/welcome.png', 'Avanthika Rajesh', 'Hi,My name is Avanthika,I am studying in amrita college of engineering')
  ];
           
} 