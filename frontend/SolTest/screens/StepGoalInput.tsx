import React, { useState } from 'react';
import { Text, TextInput, View, Button } from 'react-native';

const StepGoalInput = () => {
  const [stepGoal, setStepGoal] = useState('');

  const handleInputChange = (value: string) => {
    setStepGoal(value);
  };

  const onPress = () => {
    console.log(stepGoal);
  }

  return (
    <View>
      <Text>Entrez votre objectif de pas pour la semaine :</Text>
      <TextInput
        placeholder="Nombre de pas"
        keyboardType="numeric"
        value={stepGoal}
        onChangeText={handleInputChange}
      />
      <Button  title='Validate' onPress={onPress}></Button>
    </View>
  );
};

export default StepGoalInput;
