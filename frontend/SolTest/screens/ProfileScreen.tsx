import React, { useState } from 'react';
import {
  View,
  Text,
  Image,
  StyleSheet,
  FlatList,
} from 'react-native';
import { ProgressBar } from '@react-native-community/progress-bar-android';

interface StepsData {
  day: number;
  steps: number;
  duration: string;
}

const ProfileScreen = () => {
  const [userData, setUserData] = useState({
    name: 'John Doe',
    objectives: 5,
    profilePicture: '../assets/images/pdp.jpg',
    weeklySteps: 0.5,
  });

  const [stepsData, setStepsData] = useState<StepsData[]>([
    { day: 1, steps: 565, duration: '11:21' },
    // ... ajoutez d'autres données de pas ici
  ]);

  return (
    <View style={styles.container}>
      <View style={styles.profileSection}>
        <Image
          source={{ uri: userData.profilePicture }}
          style={styles.profileImage}
        />
        <Text style={styles.nameText}>{userData.name}</Text>
        <Text style={styles.objectivesText}>
          Objectifs atteints : {userData.objectives}
        </Text>
        
      </View>
      <View style={styles.historySection}>
        <FlatList
          data={stepsData}
          keyExtractor={(item) => item.day.toString()}
          renderItem={({ item }) => (
            <Text>
              Jour {item.day}: {item.steps} pas en {item.duration} min
            </Text>
          )}
        />
        
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  profileSection: {
    flex: 1,
    backgroundColor: '#5D63D1',
    justifyContent: 'center',
    alignItems: 'center',
  },
  profileImage: {
    width: 100,
    height: 100,
    borderRadius: 50,
  },
  nameText: {
    fontSize: 20,
    color: '#fff',
    marginVertical: 10,
  },
  objectivesText: {
    fontSize: 16,
    color: '#fff',
    marginBottom: 10,
  },
  historySection: {
    flex: 2,
    backgroundColor: '#fff',
    padding: 20,
  },
});

export default ProfileScreen;
