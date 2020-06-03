import unittest
import ui_analysis
import abstraction
import actions
from constants import *
from unittest.mock import MagicMock


class UIAnalysisTests(unittest.TestCase):

    def test_can_get_available_events_when_only_nav_and_background(self):
        # Arrange
        webdriver_mock = MagicMock(name="webdriver")
        webdriver_mock.page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        webdriver_mock.current_activity = "contactsActivity"
        current_state = ui_analysis.get_current_state(webdriver_mock)

        # Act
        available_events = ui_analysis.get_available_events(webdriver_mock)

        # Assert
        expected_available_events = [
            abstraction.create_back_event(current_state),
            abstraction.create_background_event(current_state)
        ]
        self.assertEqual(available_events, expected_available_events)

    def test_can_get_available_events_with_one_click_event(self):
        # Arrange
        webdriver_mock = MagicMock(name="webdriver")
        webdriver_mock.page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        webdriver_mock.current_activity = "contactsActivity"
        current_state = ui_analysis.get_current_state(webdriver_mock)

        # Act
        available_events = ui_analysis.get_available_events(webdriver_mock)

        # Assert
        expected_target = abstraction.create_target("id", "android:id/title1", "Display Preferences", TargetType.BUTTON, TargetState.ENABLED)
        expected_available_events = [
            {
                "precondition": current_state,
                "actions": [actions.Click(expected_target, GUIActionType.CLICK, None)]
            },
            abstraction.create_back_event(current_state),
            abstraction.create_background_event(current_state)
        ]
        self.assertEqual(available_events, expected_available_events)
    
    def test_can_identify_clickable_widgets(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        clickable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]
        actual_actionable_widgets = ui_analysis._get_actionable_widgets(page_source)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CLICK]), 2)
        self.assertEqual(clickable_widgets, actual_actionable_widgets[GUIActionType.CLICK])
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.LONG_CLICK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.UNCHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_UP]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_DOWN]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_RIGHT]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_LEFT]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.TEXT_ENTRY]), 0)

    def test_can_identify_long_clickable_widgets(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        long_clickable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]
        actual_actionable_widgets = ui_analysis._get_actionable_widgets(page_source)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.LONG_CLICK]), 2)
        self.assertEqual(long_clickable_widgets, actual_actionable_widgets[GUIActionType.LONG_CLICK])
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CLICK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.UNCHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_UP]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_DOWN]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_RIGHT]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_LEFT]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.TEXT_ENTRY]), 0)

    def test_can_identify_checkable_and_uncheckable_widgets(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        uncheckable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }]
        checkable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]
        actual_actionable_widgets = ui_analysis._get_actionable_widgets(page_source)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.UNCHECK]), 1)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CHECK]), 1)
        self.assertEqual(checkable_widgets, actual_actionable_widgets[GUIActionType.CHECK])
        self.assertEqual(uncheckable_widgets, actual_actionable_widgets[GUIActionType.UNCHECK])
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CLICK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.LONG_CLICK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_UP]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_DOWN]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.TEXT_ENTRY]), 0)

    def test_can_identify_scrollable_widgets(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        scrollable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]
        actual_actionable_widgets = ui_analysis._get_actionable_widgets(page_source)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_DOWN]), 2)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_UP]), 2)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_RIGHT]), 2)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_LEFT]), 2)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_DOWN], scrollable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_UP], scrollable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_LEFT], scrollable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_RIGHT], scrollable_widgets)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.UNCHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CLICK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.LONG_CLICK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.TEXT_ENTRY]), 0)

    def test_can_identify_enabled_text_input_widgets(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        text_entry_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "",
            "type": "EditText",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "",
            "type": "EditText",
            "state": "enabled"
        }]
        actual_actionable_widgets = ui_analysis._get_actionable_widgets(page_source)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.TEXT_ENTRY]), 2)
        self.assertEqual(actual_actionable_widgets[GUIActionType.TEXT_ENTRY], text_entry_widgets)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_DOWN]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_UP]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_RIGHT]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.SWIPE_LEFT]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.UNCHECK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.CLICK]), 0)
        self.assertEqual(len(actual_actionable_widgets[GUIActionType.LONG_CLICK]), 0)

    def test_can_identify_all_actionable_widget_types(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        scrollable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title5",
            "description": "Display Preferences",
            "type": "TextView",
            "state": "enabled"
        }]
        long_clickable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title4",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }]
        checkable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "",
            "type": "CheckBox",
            "state": "enabled"
        }]
        uncheckable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title3",
            "description": "",
            "type": "CheckBox",
            "state": "enabled"
        }]
        text_entry_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "",
            "type": "EditText",
            "state": "enabled"
        }]
        clickable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title4",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }]

        actual_actionable_widgets = ui_analysis._get_actionable_widgets(page_source)
        self.assertEqual(actual_actionable_widgets[GUIActionType.CLICK], clickable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.LONG_CLICK], long_clickable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.CHECK], checkable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.UNCHECK], uncheckable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.TEXT_ENTRY], text_entry_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_UP], scrollable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_DOWN], scrollable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_RIGHT], scrollable_widgets)
        self.assertEqual(actual_actionable_widgets[GUIActionType.SWIPE_LEFT], scrollable_widgets)

    def test_get_click_actions(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        clickable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]

        expected_actions = [
            actions.Click(clickable_widgets[0], GUIActionType.CLICK, None),
            actions.Click(clickable_widgets[1], GUIActionType.CLICK, None)
        ]
        actual_actions = ui_analysis.get_possible_actions(page_source)
        self.assertEqual(actual_actions, expected_actions)

    def test_get_long_click_actions(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        long_clickable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]

        expected_actions = [
            actions.LongClick(long_clickable_widgets[0], GUIActionType.LONG_CLICK, None),
            actions.LongClick(long_clickable_widgets[1], GUIActionType.LONG_CLICK, None)
        ]

        actual_actions = ui_analysis.get_possible_actions(page_source)
        self.assertEqual(actual_actions, expected_actions)

    def test_get_scroll_actions(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""

        scrollable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]

        expected_actions = [
            actions.SwipeDown(scrollable_widgets[0], GUIActionType.SWIPE_DOWN, None),
            actions.SwipeUp(scrollable_widgets[0], GUIActionType.SWIPE_UP, None),
            actions.SwipeRight(scrollable_widgets[0], GUIActionType.SWIPE_RIGHT, None),
            actions.SwipeLeft(scrollable_widgets[0], GUIActionType.SWIPE_LEFT, None),
            actions.SwipeDown(scrollable_widgets[1], GUIActionType.SWIPE_DOWN, None),
            actions.SwipeUp(scrollable_widgets[1], GUIActionType.SWIPE_UP, None),
            actions.SwipeRight(scrollable_widgets[1], GUIActionType.SWIPE_RIGHT, None),
            actions.SwipeLeft(scrollable_widgets[1], GUIActionType.SWIPE_LEFT, None)
        ]
        actual_actions = ui_analysis.get_possible_actions(page_source)
        self.assertIn(expected_actions[0], actual_actions)
        self.assertIn(expected_actions[1], actual_actions)
        self.assertIn(expected_actions[2], actual_actions)
        self.assertIn(expected_actions[3], actual_actions)
        self.assertIn(expected_actions[4], actual_actions)
        self.assertIn(expected_actions[5], actual_actions)
        self.assertIn(expected_actions[6], actual_actions)
        self.assertIn(expected_actions[7], actual_actions)

    def test_get_check_actions(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        uncheckable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }]
        checkable_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "Login",
            "type": "TextView",
            "state": "enabled"
        }]

        expected_actions = [
            actions.Click(uncheckable_widgets[0], GUIActionType.UNCHECK, None),
            actions.Click(checkable_widgets[0], GUIActionType.CHECK, None)
        ]
        actual_actions = ui_analysis.get_possible_actions(page_source)
        self.assertIn(expected_actions[0], actual_actions)
        self.assertIn(expected_actions[1], actual_actions)

    def test_get_text_entry_actions(self):
        page_source = """<?xml version='1.0' encoding='UTF-8' standalone='yes' ?>
<hierarchy index="0" class="hierarchy" rotation="0" width="720" height="1184">
  <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
    <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,0][720,1184]" displayed="true">
      <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
        <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/decor_content_parent" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,1184]" displayed="true">
          <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="org.traccar.client:id/action_bar_container" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
            <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/action_bar" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,50][720,162]" displayed="true">
              <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Traccar Client" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[32,79][280,133]" displayed="true" />
              <androidx.appcompat.widget.LinearLayoutCompat index="1" package="org.traccar.client" class="androidx.appcompat.widget.LinearLayoutCompat" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,50][720,162]" displayed="true">
                <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Status" resource-id="org.traccar.client:id/status" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[587,58][720,154]" displayed="true" />
              </androidx.appcompat.widget.LinearLayoutCompat>
            </android.view.View>
          </android.widget.FrameLayout>
          <android.widget.FrameLayout index="1" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/content" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
            <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
              <android.widget.FrameLayout index="0" package="org.traccar.client" class="android.widget.FrameLayout" text="" resource-id="android:id/action_menu_presenter" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,1184]" displayed="true">
                <android.view.View index="0" package="org.traccar.client" class="android.view.View" text="" resource-id="org.traccar.client:id/recycler_view" checkable="false" checked="false" clickable="false" enabled="true" focusable="true" focused="true" long-clickable="false" password="false" scrollable="true" selected="false" bounds="[0,162][720,1184]" displayed="true">
                  <android.widget.LinearLayout index="0" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,162][720,307]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,162][562,307]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Service status" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,194][346,237]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Service stopped" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,237][345,275]" displayed="true" />
                    </android.widget.RelativeLayout>
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[562,162][688,307]" displayed="true">
                      <android.widget.Switch index="0" package="org.traccar.client" class="android.widget.Switch" text="Start" resource-id="android:id/overflow_menu_presenter" checkable="true" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[594,207][688,261]" displayed="true" />
                    </android.widget.LinearLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,307][720,452]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,307][688,452]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Device identifier" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,339][373,382]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="587133" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,382][240,420]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="2" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,452][720,597]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,452][688,597]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Server URL" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,484][301,527]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Tracking server URL" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,527][390,565]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="3" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,597][720,742]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,597][688,742]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Location accuracy" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,629][403,672]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Desired location accuracy" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,672][463,710]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="4" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,742][720,887]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,742][688,887]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Frequency" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,774][293,817]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting interval in seconds" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,817][504,855]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="5" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,887][720,1032]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,887][688,1032]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Distance" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,919][269,962]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting distance in meters" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,962][501,1000]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="6" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1032][720,1177]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1032][688,1177]" displayed="true">
                      <android.widget.TextView index="0" package="org.traccar.client" class="android.widget.TextView" text="Angle" resource-id="android:id/title" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1064][226,1107]" displayed="true" />
                      <android.widget.TextView index="1" package="org.traccar.client" class="android.widget.TextView" text="Reporting angle in degrees" resource-id="android:id/summary" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1107][476,1145]" displayed="true" />
                    </android.widget.RelativeLayout>
                  </android.widget.LinearLayout>
                  <android.widget.LinearLayout index="7" package="org.traccar.client" class="android.widget.LinearLayout" text="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[0,1177][720,1184]" displayed="true">
                    <android.widget.RelativeLayout index="0" package="org.traccar.client" class="android.widget.RelativeLayout" text="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[144,1177][592,1184]" displayed="true" />
                    <android.widget.LinearLayout index="1" package="org.traccar.client" class="android.widget.LinearLayout" text="" resource-id="android:id/widget_frame" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" long-clickable="false" password="false" scrollable="false" selected="false" bounds="[592,1177][688,1184]" displayed="true" />
                  </android.widget.LinearLayout>
                </android.view.View>
              </android.widget.FrameLayout>
            </android.widget.LinearLayout>
          </android.widget.FrameLayout>
        </android.view.View>
      </android.widget.FrameLayout>
    </android.widget.LinearLayout>
  </android.widget.FrameLayout>
</hierarchy>
"""
        text_entry_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "",
            "type": "EditText",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "",
            "type": "EditText",
            "state": "enabled"
        }]
        expected_actions = [
            actions.TextEntry(text_entry_widgets[0], GUIActionType.TEXT_ENTRY, None),
            actions.TextEntry(text_entry_widgets[1], GUIActionType.TEXT_ENTRY, None)
        ]
        actual_actions = ui_analysis.get_possible_actions(page_source)
        self.assertIn(expected_actions[0], actual_actions)
        self.assertIn(expected_actions[1], actual_actions)

    def test_classify_actions(self):
        text_entry_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/title1",
            "description": "",
            "type": "EditText",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/title2",
            "description": "",
            "type": "EditText",
            "state": "enabled"
        }]

        non_text_entry_widgets = [{
            "selector": "id",
            "selectorValue": "android:id/btn1",
            "description": "Display Preferences",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/btn2",
            "description": "Login",
            "type": "Button",
            "state": "enabled"
        }, {
            "selector": "id",
            "selectorValue": "android:id/checkbox1",
            "description": "Show All",
            "type": "CheckBox",
            "state": "enabled"
        }]

        possible_actions = [
            actions.TextEntry(text_entry_widgets[0], GUIActionType.TEXT_ENTRY, None),
            actions.TextEntry(text_entry_widgets[1], GUIActionType.TEXT_ENTRY, None),
            actions.Click(non_text_entry_widgets[0], GUIActionType.CLICK, None),
            actions.Click(non_text_entry_widgets[1], GUIActionType.CLICK, None),
            actions.Click(non_text_entry_widgets[2], GUIActionType.CHECK, None),
            actions.Click(non_text_entry_widgets[2], GUIActionType.UNCHECK, None)
        ]

        expected_text_entry_actions = [
            actions.TextEntry(text_entry_widgets[0], GUIActionType.TEXT_ENTRY, None),
            actions.TextEntry(text_entry_widgets[1], GUIActionType.TEXT_ENTRY, None)
        ]

        expected_non_text_entry_actions = [
            actions.Click(non_text_entry_widgets[0], GUIActionType.CLICK, None),
            actions.Click(non_text_entry_widgets[1], GUIActionType.CLICK, None),
            actions.Click(non_text_entry_widgets[2], GUIActionType.CHECK, None),
            actions.Click(non_text_entry_widgets[2], GUIActionType.UNCHECK, None)
        ]
        text_entry_actions, non_text_entry_actions = ui_analysis.classify_actions(possible_actions)
        self.assertEqual(text_entry_actions, expected_text_entry_actions)
        self.assertEqual(non_text_entry_actions, expected_non_text_entry_actions)
