import React, {useState} from 'react';
import {View, Text, TouchableOpacity, StyleSheet} from 'react-native';
import {GoogleSignin, GoogleSigninButton} from '@react-native-google-signin/google-signin';

GoogleSignin.configure({
  webClientId: '<VOTRE_ID_CLIENT_WEB>',
});

const First = () => {
  const [selectedSteps, setSelectedSteps] = useState(0);

  const signIn = async () => {
    try {
      await GoogleSignin.hasPlayServices();
      const userInfo = await GoogleSignin.signIn();
      // Ici, vous pouvez utiliser les informations de l'utilisateur pour vous inscrire ou vous connecter
    } catch (error) {
      console.error(error);
    }
  };

  const stepsOptions = [3000, 7000, 15000];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Choisissez le nombre de pas :</Text>
      {stepsOptions.map((steps, index) => (
        <TouchableOpacity
          key={index}
          style={[
            styles.stepsButton,
            selectedSteps === steps ? styles.selected : {},
          ]}
          onPress={() => setSelectedSteps(steps)}>
          <Text style={styles.stepsButtonText}>{steps}</Text>
        </TouchableOpacity>
      ))}
      <GoogleSigninButton
        style={styles.googleButton}
        size={GoogleSigninButton.Size.Wide}
        color={GoogleSigninButton.Color.Dark}
        onPress={signIn}
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
  stepsButton: {
    backgroundColor: '#DDDDDD',
    padding: 10,
    borderRadius: 5,
    marginVertical: 5,
  },
  stepsButtonText: {
    fontSize: 18,
  },
  selected: {
    backgroundColor: '#2196F3',
  },
  googleButton: {
    marginTop: 20,
  },
});

export default First;
