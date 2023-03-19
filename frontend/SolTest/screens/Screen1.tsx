import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, TextInput } from 'react-native';
import { StackNavigationProp } from '@react-navigation/stack';

type Screen1NavigationProp = StackNavigationProp<any, 'Screen1'>;

interface Screen1Props {
  navigation: Screen1NavigationProp;
}

const Screen1 :React.FC<Screen1Props> = ({navigation}) => {
    const [selectedStepChallenge, setSelectedStepChallenge] = useState(null);
    const [solanaAmount, setSolanaAmount] = useState('');
  
    const stepChallenges = [
      { label: '3000 Steps', value: 3000 },
      { label: '7000 Steps', value: 7000 },
      { label: '15000+ Steps', value: 15000 },
    ];
  
    const handleChallengeSelection = (value : any) => {
        console.log(value);
      setSelectedStepChallenge(value);
    };
  
    const handleValidation = () => {
      // TODO: Implement your logic for submitting the challenge and payment here
      navigation.navigate('Screen2');
      console.log('Selected step challenge:', selectedStepChallenge);
      console.log('Solana amount:', solanaAmount);
    };
  
    return (
      <View style={styles.container}>
        <Text style={styles.title}>Select Step Challenge</Text>
        <View style={styles.challengeList}>
          {stepChallenges.map((challenge, index) => (
            <TouchableOpacity
              key={index}
              style={[
                styles.challengeButton,
                selectedStepChallenge === challenge.value && styles.selectedChallengeButton,
              ]}
              onPress={() => handleChallengeSelection(challenge.value)}
            >
              <Text
                style={[
                  styles.challengeText,
                  selectedStepChallenge === challenge.value && styles.selectedChallengeText,
                ]}
              >
                {challenge.label}
              </Text>
            </TouchableOpacity>
          ))}
        </View>
        <Text style={styles.inputLabel}>Enter Solana Amount:</Text>
        <TextInput
          style={styles.input}
          keyboardType="numeric"
          placeholder="0.0"
          onChangeText={(text) => setSolanaAmount(text)}
          value={solanaAmount}
        />
        <TouchableOpacity onPress={handleValidation} style={styles.validateButton}>
          <Text style={styles.buttonText}>Validate</Text>
        </TouchableOpacity>
      </View>
    );
  };
  

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      paddingHorizontal: 20,
    },
    title: {
      fontSize: 24,
      fontWeight: 'bold',
      textAlign: 'center',
      marginBottom: 20,
    },
    challengeList: {
      flexDirection: 'row',
      justifyContent: 'space-around',
      marginBottom: 20,
    },
    challengeButton: {
      padding: 10,
      backgroundColor: '#ccc',
      borderRadius: 5,
    },
    selectedChallengeButton: {
      backgroundColor: '#007AFF',
    },
    challengeText: {
      fontSize: 18,
    },
    selectedChallengeText: {
      color: '#fff',
    },
    inputLabel: {
      fontSize: 18,
      marginBottom: 5,
    },
    input: {
      borderWidth: 1,
      borderColor: '#ccc',
      borderRadius: 5,
      paddingHorizontal: 10,
      paddingVertical: 5,
      fontSize: 18,
      marginBottom: 20,
    },
    validateButton: {
        backgroundColor: '#007AFF',
        borderRadius: 5,
        paddingVertical: 10,
        paddingHorizontal: 20,
        alignSelf: 'center',
      },
      buttonText: {
        fontSize: 18,
        color: '#fff',
      },
    });
    
  
export default Screen1;
