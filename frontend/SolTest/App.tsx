import React, { Component, useEffect, useState} from 'react';
import type { PropsWithChildren } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import EntypoIcon from 'react-native-vector-icons/Entypo';
import FontAwesomeIcon from 'react-native-vector-icons/FontAwesome';
import {
  Button,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
} from 'react-native';

import { SafeAreaProvider } from 'react-native-safe-area-context';

import {
  Colors,
  DebugInstructions,
  LearnMoreLinks,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

import Header from './screens/Header';
import StepGoalInput from './screens/StepGoalInput';
import { Keypair, Connection, clusterApiUrl } from '@solana/web3.js';
import { Wallet } from './screens/Wallet';
import ProfileScreen from './screens/ProfileScreen';
import First from './screens/First';
import Screen1 from './screens/Screen1';
import Screen2 from './screens/Screen2';

type SectionProps = PropsWithChildren<{
  title: string;
}>;

const Stack = createNativeStackNavigator();

const Section = ({ children, title }: SectionProps)=>  {
  const isDarkMode = useColorScheme() === 'dark';
  return (
    <View style={styles.sectionContainer}>
      <Text
        style={[
          styles.sectionTitle,
          {
            color: isDarkMode ? Colors.white : Colors.black,
          },
        ]}
      >
        {title}
      </Text>
      <Text
        style={[
          styles.sectionDescription,
          {
            color: isDarkMode ? Colors.light : Colors.dark,
          },
        ]}
      >
        {children}
      </Text>
    </View>
  );
}
const Tab = createBottomTabNavigator();

const  App = () =>  {
  const isDarkMode = useColorScheme() === 'dark';

  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  const [keypair, setKeypair] = useState<Keypair>(() => Keypair.generate());
  const randomKeypair = () => {
  setKeypair(() => Keypair.generate());
  };

  const [version, setVersion] = useState<any>('');
  useEffect(() => {
  const conn = new Connection(clusterApiUrl('devnet'));
  conn.getVersion().then(r => {
    setVersion(r);
  });
}, []);




  return (
   
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            if (route.name === 'Screen1') {
              return <FontAwesomeIcon name="home" size={size} color={color} />;
            } else if (route.name === 'Screen2') {
              return <EntypoIcon name="share" size={size} color={color} />;
            }
          },
        })}
      
      >
        <Tab.Screen
          name="Screen1"
          component={Screen1}
          options={{ title: '' }}
        />
        <Tab.Screen
          name="Screen2"
          component={Screen2}
          options={{ title: '' }}
        />
      </Tab.Navigator>
    </NavigationContainer>
          



    
        
   
  );
}

const styles = StyleSheet.create({
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
});

export default App;
