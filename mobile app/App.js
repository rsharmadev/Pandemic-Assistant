import * as React from 'react';
import { Text, View, StyleSheet, Image, ScrollView } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { WebView } from 'react-native-webview';
import { Ionicons } from '@expo/vector-icons';
import { TextInput } from 'react-native-gesture-handler';

let i = 0;



function HomeScreen() {
  return (
<View style={{flex: 1}}>
   <WebView
      automaticallyAdjustContentInsets={false}
      source={{uri: 'https://cnn.com'}}
   />
</View>
  );
}

function webScreen() {
  return (
    <View style={{flex: 1}}>
      <WebView style={{marginTop: 30}}
      automaticallyAdjustContentInsets={false}
      source={{uri: "http://192.168.1.153:11000"}}

      />
    </View>
  )
}

function dScreen() {
  let WebViewRef;

  return (
    <View style={{flex: 1}}>
      <WebView style={{marginTop: 30}}
      ref={WEBVIEW_REF => {WebViewRef = WEBVIEW_REF}}
      automaticallyAdjustContentInsets={false}
      source={{uri: "https://landing.google.com/screener/covid19"}}
      onLoad = {a => { if(i==0) {WebViewRef.reload(); console.log(i); i+=1; console.log(i) } } }
      />
    </View>
  );
}



const Tab = createBottomTabNavigator();

function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            if (route.name === 'News') {
              return (
                <Ionicons
                  name={
                    focused
                      ? 'ios-information-circle'
                      : 'ios-information-circle-outline'
                  }
                  size={size}
                  color={color}
                />
              );
            } else if (route.name === 'Diagnostic') {
              return (
                <Ionicons
                  name={focused ? 'ios-list-box' : 'ios-list'}
                  size={size}
                  color={color}
                />
              );
            } else if (route.name === 'Map') {
              return (
                <Ionicons
                  name={focused ? 'ios-map': 'ios-map'}
                  size={size}
                  color={color}
                  />
              );
            }
          },
        })}
        tabBarOptions={{
          activeTintColor: 'white',
          style: {
            backgroundColor: '#310f3a'
          }
        }}
      >
        <Tab.Screen name="News" component={HomeScreen} options={{ tabBarBadge: null }}/>
        <Tab.Screen name="Diagnostic" component={dScreen} options={{ tabBarBadge: null }}/>
        <Tab.Screen name="Map" component={webScreen} options={{ tabBarBadge: null }}/>
      </Tab.Navigator>
    </NavigationContainer>
  )
}

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#310f3a',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    position: 'absolute',
    top: 60,
    color: "#E7E1E1",
    fontSize: 30,
    fontWeight: 'bold',
    alignItems: 'center',
    justifyContent: 'center'
  },
  bodyy: {
    position: 'absolute',
    color: "#E7E1E1",

    top: 120
  },
  images: {
    position: 'absolute',
    width: 200,
    height: 200,
    top: 300,
    borderRadius: 30
  },
  input: {
    borderColor: '#FFFFFF'
  }
});
