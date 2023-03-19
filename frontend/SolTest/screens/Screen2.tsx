import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';

type Screen2NavigationProp = StackNavigationProp<any, 'Screen2'>;

interface Screen2Props {
  navigation: Screen2NavigationProp;
}

const Screen2: React.FC<Screen2Props> = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Écran 2</Text>
      <Button
        title="Retourner à l'écran 1"
        onPress={() => navigation.navigate('Screen1')}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  title: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
});

export default Screen2;
